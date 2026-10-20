import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch


def module(name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).resolve().parents[1] / (name + '.py'))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


sync = module('sync_drive')
docs = module('check_docs')


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.dest = self.root / 'docs/Week01/Material/a.md'
        self.dest.parent.mkdir(parents=True)
        self.incoming = self.root / '.agents/scripts/.sync_incoming'
        self.remote = b'remote revision'

    def download(self, name, file_id, path):
        Path(path).write_bytes(self.remote)

    def baseline(self, content=b'baseline'):
        return {'hash': hashlib.sha256(content).hexdigest(),
                'dest_path': self.dest.relative_to(self.root).as_posix()}

    def run_sync(self, base=None, downloader=None):
        with contextlib.redirect_stdout(io.StringIO()):
            return sync.sync_one('a.md', 'abc123', self.dest, base, self.incoming, self.root, downloader or self.download)

    def test_new_file(self):
        status, meta = self.run_sync()
        self.assertEqual(status, 'updated')
        self.assertEqual(self.dest.read_bytes(), self.remote)
        self.assertEqual(meta['hash'], hashlib.sha256(self.remote).hexdigest())

    def test_remote_update_is_not_skipped_when_local_equals_baseline(self):
        self.dest.write_bytes(b'baseline')
        self.assertEqual(self.run_sync(self.baseline())[0], 'updated')
        self.assertEqual(self.dest.read_bytes(), self.remote)

    def test_local_edit_is_preserved_even_when_remote_unchanged(self):
        self.remote = b'baseline'
        self.dest.write_bytes(b'local edit')
        self.assertEqual(self.run_sync(self.baseline()), ('conflict', None))
        self.assertEqual(self.dest.read_bytes(), b'local edit')
        self.assertEqual(next(self.incoming.rglob('a.md')).read_bytes(), b'baseline')

    def test_existing_without_baseline_is_preserved(self):
        self.dest.write_bytes(b'reviewed')
        self.assertEqual(self.run_sync()[0], 'conflict')
        self.assertEqual(self.dest.read_bytes(), b'reviewed')

    def test_equal_content_can_establish_baseline(self):
        self.dest.write_bytes(self.remote)
        self.assertEqual(self.run_sync()[0], 'unchanged')

    def test_deleted_local_file_is_not_recreated(self):
        self.assertEqual(self.run_sync(self.baseline())[0], 'conflict')
        self.assertFalse(self.dest.exists())

    def test_submission_protected_even_with_clean_baseline(self):
        self.dest = self.root / 'docs/Week01/Submission/a.md'
        self.dest.parent.mkdir(parents=True)
        self.dest.write_bytes(b'baseline')
        self.assertEqual(self.run_sync(self.baseline())[0], 'conflict')
        self.assertEqual(self.dest.read_bytes(), b'baseline')

    def test_edit_during_download_is_preserved(self):
        def download(name, file_id, path):
            self.download(name, file_id, path)
            self.dest.write_bytes(b'concurrent edit')
        self.assertEqual(self.run_sync(downloader=download)[0], 'conflict')
        self.assertEqual(self.dest.read_bytes(), b'concurrent edit')

    def test_download_failure_keeps_original_and_cleans_temp(self):
        self.dest.write_bytes(b'local')
        def failure(*args):
            Path(args[-1]).write_bytes(b'partial')
            raise OSError('offline')
        with self.assertRaises(OSError):
            self.run_sync(downloader=failure)
        self.assertEqual(self.dest.read_bytes(), b'local')
        self.assertEqual(list(self.incoming.iterdir()), [])

    def test_pull_failure_stops_before_fetch(self):
        with patch.object(sync, 'ROOT', self.root), patch.object(sync, 'run_git_pull', side_effect=RuntimeError('failed')), patch.object(sync, 'fetch_folder_html') as fetch, contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(sync.main(['--pull']), 1)
            fetch.assert_not_called()

    def test_dirty_tree_does_not_pull(self):
        with patch.object(sync.subprocess, 'check_output', return_value=b' M a.md'), patch.object(sync.subprocess, 'run') as run:
            with self.assertRaises(RuntimeError):
                sync.run_git_pull(self.root)
            run.assert_not_called()

    def test_download_error_has_nonzero_exit_and_no_false_success(self):
        with patch.object(sync, 'ROOT', self.root), patch.object(sync, 'fetch_folder_html', return_value='html'), patch.object(sync, 'extract_files_from_html', return_value={'a.md': 'abc123'}), patch.object(sync, 'sync_one', side_effect=OSError('offline')), contextlib.redirect_stdout(io.StringIO()) as output, contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(sync.main([]), 1)
            self.assertIn('error=1', output.getvalue())
            self.assertNotIn('mới nhất', output.getvalue())

    def test_empty_listing_is_not_success(self):
        with patch.object(sync, 'ROOT', self.root), patch.object(sync, 'fetch_folder_html', return_value='login'), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(sync.main([]), 1)

    def test_bad_names_rejected(self):
        for name in ['../a.md', '/tmp/a.md', 'folder\\a.md', '..']:
            with self.assertRaises(ValueError):
                sync.valid_name(name)

    def test_login_page_rejected(self):
        with self.assertRaises(ValueError):
            sync.validate_download(b'<!DOCTYPE html><html>ServiceLogin</html>', '.md')

    def test_template_not_classified_as_proposal(self):
        self.assertEqual(sync.classify_destination('Template-ProjectProposal.pdf', Path('docs/Week01')), Path('docs/Week01/Material'))


class DocumentTests(unittest.TestCase):
    def test_missing_image_and_encoded_hash(self):
        present = {'docs/image/a.png', 'docs/Template#0.pdf'}
        self.assertIsNone(docs.check_link('docs/a.md', './Template%230.pdf', present.__contains__))
        self.assertIsNone(docs.check_link('docs/a.md', './image/a.png', present.__contains__))
        self.assertIsNotNone(docs.check_link('docs/a.md', './image/lost.png', present.__contains__))

    def test_examples_not_checked_as_live_links(self):
        text = '```md\n[example](missing.md)\n```\n[real](a.md)\n<img src="image/a.png">'
        self.assertEqual(set(docs.links(text, '.md')), {'a.md', 'image/a.png'})

    def test_content_drift(self):
        self.assertFalse(docs.pair_warning('# Hello\n\nFour modules.', '<h1>Hello</h1><p>Four modules.</p>'))
        self.assertTrue(docs.pair_warning('# New scope\nDeepSeek four modules', '<h1>Old architecture</h1><p>Gemini dispatcher five subsystems</p>'))

    def test_staged_checks_index_not_worktree(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def git(*args):
                return subprocess.run(['git', *args], cwd=root, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            git('init')
            (root/'a.md').write_text('[image](missing.png)')
            git('add', 'a.md')
            # Unstaged repair must not make the staged invalid document pass.
            (root/'a.md').write_text('repaired locally')
            (root/'missing.png').write_bytes(b'not staged')
            with patch.object(docs, 'ROOT', root), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(docs.main(['--staged']), 1)
            git('add', 'missing.png')
            with patch.object(docs, 'ROOT', root), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(docs.main(['--staged']), 0)


if __name__ == '__main__':
    unittest.main()
