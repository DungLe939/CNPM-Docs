#!/usr/bin/env python3
"""Check local document links in the working tree or Git index (standard library)."""
import argparse
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
import posixpath
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


class DocumentHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.words = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        if tag in {'script', 'style'}:
            self.hidden += 1
        for key, value in attrs:
            if key in {'href', 'src'} and value:
                self.links.append(value)

    def handle_endtag(self, tag):
        if tag in {'script', 'style'}:
            self.hidden = max(0, self.hidden - 1)

    def handle_data(self, data):
        if not self.hidden:
            self.words.append(data)


def strip_fences(text):
    return re.sub(r'(?ms)^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1\s*$', '', text)


def links(text, suffix):
    if suffix == '.md':
        text = strip_fences(text)
    parser = DocumentHTML()
    parser.feed(text)
    targets = parser.links
    if suffix == '.md':
        # Inline links and reference definitions; code samples aren't live links.
        text = re.sub(r'`[^`\n]+`', '', text)
        targets += [m[0] or m[1] for m in re.findall(
            r'\]\(\s*(?:<([^>]+)>|([^\s)]+))(?:\s+["\'][^\n]*?["\'])?\s*\)', text)]
        targets += re.findall(r'(?m)^\s*\[[^\]]+\]:\s*<?([^\s>]+)>?', text)
    return targets


def check_link(source, target, exists):
    if target.startswith(('#', '//')):
        return None
    if re.match(r'^[A-Za-z]:[/\\]', target):
        return 'đường dẫn tuyệt đối'
    url = urlsplit(target)
    if url.scheme:
        return 'đường dẫn file tuyệt đối' if url.scheme == 'file' else None
    path = unquote(url.path)
    if not path:
        return None
    if path.startswith('/'):
        return 'đường dẫn tuyệt đối'
    local = posixpath.normpath(posixpath.join(posixpath.dirname(source), path))
    if local == '..' or local.startswith('../'):
        return 'đường dẫn ra ngoài repo'
    if not exists(local):
        return 'thiếu file/ảnh local'
    return None


def prose(text, suffix):
    if suffix == '.html':
        parser = DocumentHTML(); parser.feed(text)
        text = ' '.join(parser.words)
    else:
        text = re.sub(r'\A---\n.*?\n---\n', '', text, flags=re.S)
        text = strip_fences(text)
        text = re.sub(r'!?\[([^\]]*)\]\([^)]+\)', r'\1', text)
        text = re.sub(r'<[^>]*>', '', text)
    return Counter(re.findall(r'\w+', text.lower()))


def pair_warning(markdown, html):
    a, b = prose(markdown, '.md'), prose(html, '.html')
    common = sum((a & b).values())
    total = sum(a.values()) + sum(b.values())
    return bool(total and 2 * common / total < .85)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--staged', action='store_true')
    args = parser.parse_args(argv)
    tracked = {p for p in git('ls-files', '-z').decode().split('\0') if p}
    if args.staged:
        changed = {p for p in git('diff', '--cached', '--name-only', '-z').decode().split('\0') if p}
        deleted = {p for p in git('diff', '--cached', '--diff-filter=D', '--name-only', '-z').decode().split('\0') if p}
        selected = tracked if deleted else changed
        read = lambda name: git('show', ':' + name).decode('utf-8')
        exists = lambda name: name in tracked or any(p.startswith(name.rstrip('/') + '/') for p in tracked)
    else:
        untracked = {p for p in git('ls-files', '--others', '--exclude-standard', '-z').decode().split('\0') if p}
        selected = tracked | untracked
        changed = selected
        read = lambda name: (ROOT / name).read_text()
        exists = lambda name: (ROOT / name).exists()
    errors, warnings = [], []
    documents = sorted(p for p in selected if PurePosixPath(p).suffix in {'.md', '.html'} and exists(p))
    for name in documents:
        try:
            content = read(name)
            for target in links(content, PurePosixPath(name).suffix):
                error = check_link(name, target, exists)
                if error:
                    errors.append(f'{name}: {error}: {target}')
            if name.endswith('.md'):
                other = name[:-3] + '.html'
                if exists(other):
                    if pair_warning(content, read(other)):
                        warnings.append(f'{name}: nội dung Markdown/HTML có độ lệch lớn, cần đối chiếu.')
            if args.staged:
                other = str(PurePosixPath(name).with_suffix('.html' if name.endswith('.md') else '.md'))
                if name in changed and exists(other) and other not in changed:
                    warnings.append(f'{name}: bản tương ứng {other} không staged, xác nhận thay đổi có cần đồng bộ.')
        except (OSError, UnicodeError, subprocess.CalledProcessError, ValueError) as exc:
            errors.append(f'{name}: không kiểm tra được: {exc}')
    for message in errors:
        print('ERROR: ' + message)
    for message in sorted(set(warnings)):
        print('WARN: ' + message)
    print(f'Checked {len(documents)} documents: {len(errors)} errors, {len(set(warnings))} warnings.')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
