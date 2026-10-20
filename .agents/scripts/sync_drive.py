#!/usr/bin/env python3
"""Compare public Drive downloads with local files without overwriting local edits."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_FOLDER_ID = "12e0__KnGQOQayRmNEWwYPrq-0ErlqGph"
USER_AGENT = "Mozilla/5.0"


def run_git_pull(root):
    if subprocess.check_output(["git", "status", "--porcelain"], cwd=root).strip():
        raise RuntimeError("Working tree có thay đổi. Giữ nguyên local, chưa pull/sync.")
    branch = subprocess.check_output(
        ["git", "symbolic-ref", "--quiet", "--short", "HEAD"], cwd=root, text=True
    ).strip()
    subprocess.run(["git", "pull", "--ff-only", "origin", branch], cwd=root, check=True)


def fetch_folder_html(folder_id):
    req = urllib.request.Request(
        f"https://drive.google.com/drive/folders/{folder_id}", headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.read().decode("utf-8")


def extract_files_from_html(html):
    """Trích xuất danh sách file (tên và ID) từ HTML của Google Drive."""
    files = {}

    # Pattern 1: aria-label chứa tên file + loại file + ssk chứa ID
    p1 = r'aria-label=[\'\"]([^\'\"]+?)\s+(?:Markdown|HTML|Document|Spreadsheet|PDF|Shared|Text|Word|Zip|File)[^\'\"]*[\'\"]\s+[^>]*?ssk=[\'\"][^:\'\"]*:[^:\'\"]*:([a-zA-Z0-9_-]{25,})'
    for name, raw_id in re.findall(p1, html):
        clean_id = re.sub(r'-\d+-\d+$', '', raw_id)
        name_clean = name.strip()
        if name_clean and clean_id:
            files[name_clean] = clean_id

    # Pattern 2: aria-label chứa file name và đuôi mở rộng
    p2 = r'aria-label=[\'\"]([a-zA-Z0-9_\-\. ]+\.[a-zA-Z0-9]{2,5})[^\'\"]*[\'\"][^>]*?ssk=[\'\"][^:\'\"]*:[^:\'\"]*:([a-zA-Z0-9_-]{25,})'
    for name, raw_id in re.findall(p2, html):
        clean_id = re.sub(r'-\d+-\d+$', '', raw_id)
        name_clean = name.strip()
        if name_clean and clean_id and name_clean not in files:
            files[name_clean] = clean_id

    return files



def valid_name(name):
    if not name or name in {".", ".."} or any(c in name for c in "/\\\0"):
        raise ValueError("Tên file nguồn không hợp lệ")
    return name


def validate_download(content, suffix):
    if not content:
        raise ValueError("File tải về trống")
    head = content[:8192].lower()
    if b"servicelogin" in head or b"accounts.google.com/v3/signin" in head:
        raise ValueError("Drive yêu cầu đăng nhập")
    looks_html = b"<!doctype html" in head or b"<html" in head
    if looks_html and suffix not in {".html", ".htm"}:
        raise ValueError("Nhận trang HTML thay vì tài liệu")
    if suffix == ".pdf" and not content.startswith(b"%PDF-"):
        raise ValueError("Nội dung không phải PDF")
    if suffix == ".docx" and not content.startswith(b"PK"):
        raise ValueError("Nội dung không phải DOCX")


def download_file(name, file_id, temp_path):
    suffix = Path(name).suffix.lower()
    export_format = {".docx": "docx", ".pdf": "pdf", ".html": "html"}.get(suffix, "txt")
    urls = [f"https://drive.usercontent.google.com/download?id={file_id}&export=download",
            f"https://docs.google.com/document/d/{file_id}/export?format={export_format}"]
    last_error = None
    for url in urls:
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=30) as response:
                content = response.read()
            validate_download(content, suffix)
            Path(temp_path).write_bytes(content)
            return
        except Exception as exc:
            last_error = exc
    raise RuntimeError(f"Không tải được {name}: {last_error}")


def classify_destination(name, week_dir):
    lower = name.lower()
    # A template whose name includes 'Proposal' is still course material.
    groups = [(('template', 'thong_bao', 'material', 'tai_lieu'), 'Material'),
              (('meeting', 'bien_ban', 'hop_nhom'), 'Team_Decision'),
              (('problem', 'example', 'bai_toan', 'de_bai'), 'Problem_example'),
              (('hireus', 'plan', 'proposal', 'jobseeker', 'decision'), 'Team_Decision/Material')]
    for keys, folder in groups:
        if any(key in lower for key in keys):
            return Path(week_dir) / folder
    return Path(week_dir) / 'Unclassified'


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def atomic_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent, delete=False) as f:
        temp = Path(f.name)
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    try:
        os.replace(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def sync_one(name, file_id, destination, baseline, incoming, root, downloader=download_file):
    valid_name(name)
    if not re.fullmatch(r'[a-zA-Z0-9_-]+', file_id):
        raise ValueError('ID nguồn không hợp lệ')
    root = Path(root).resolve()
    dest = Path(destination)
    if dest.is_symlink() or not dest.resolve().is_relative_to(root):
        raise ValueError('Đích không được trỏ ra ngoài dự án hoặc qua symlink file')
    dest = dest.resolve()
    relative = dest.relative_to(root).as_posix()
    original_hash = file_hash(dest) if dest.exists() else None
    incoming = Path(incoming).resolve()
    incoming.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=incoming, delete=False) as f:
        temp = Path(f.name)
    try:
        downloader(name, file_id, temp)
        remote_hash = file_hash(temp)
        current_hash = file_hash(dest) if dest.exists() else None
        metadata = {'name': name, 'file_id': file_id, 'hash': remote_hash, 'dest_path': relative}
        if current_hash != original_hash:
            status = 'conflict'
        elif current_hash == remote_hash:
            return 'unchanged', metadata
        elif 'Submission' in dest.relative_to(root).parts:
            status = 'conflict'
        elif baseline and baseline.get('dest_path') != relative:
            status = 'conflict'
        elif current_hash is None and not baseline:
            status = 'updated'
        elif current_hash is not None and baseline and current_hash == baseline.get('hash'):
            status = 'updated'
        else:
            status = 'conflict'
        if status == 'conflict':
            saved = incoming / file_id / remote_hash / name
            saved.parent.mkdir(parents=True, exist_ok=True)
            os.replace(temp, saved)
            print(f'  Bản chờ đối chiếu: {saved.relative_to(root)}')
            return status, None
        dest.parent.mkdir(parents=True, exist_ok=True)
        # Do not replace a file edited while the network request was in flight.
        if dest.is_symlink() or not dest.resolve().is_relative_to(root):
            raise ValueError('Đường dẫn đích đã thay đổi')
        if (file_hash(dest) if dest.exists() else None) != original_hash:
            raise RuntimeError('File local vừa thay đổi, dừng ghi')
        os.replace(temp, dest)
        return status, metadata
    finally:
        temp.unlink(missing_ok=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--folder', default=DEFAULT_FOLDER_ID)
    parser.add_argument('--week', default='Week01')
    parser.add_argument('--target')
    parser.add_argument('--pull', action='store_true')
    args = parser.parse_args(argv)
    if not re.fullmatch(r'Week[0-9]{2}', args.week):
        parser.error('--week phải có dạng Week01')
    if not re.fullmatch(r'[a-zA-Z0-9_-]+', args.folder):
        parser.error('--folder phải là ID Drive')
    target = (ROOT / (args.target or f'docs/{args.week}')).resolve()
    if not target.is_relative_to(ROOT.resolve() / 'docs'):
        parser.error('--target phải nằm trong docs/ của dự án')
    manifest_path = ROOT / '.agents/scripts/.sync_manifest.json'
    incoming = ROOT / '.agents/scripts/.sync_incoming'
    try:
        if args.pull:
            run_git_pull(ROOT)
        manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
        if not isinstance(manifest, dict):
            raise ValueError('Manifest không hợp lệ')
        files = extract_files_from_html(fetch_folder_html(args.folder))
        if not files:
            raise RuntimeError('Không nhận diện được file. Chưa xác nhận thư mục trống hay đã đồng bộ.')
        counts = dict(updated=0, unchanged=0, conflict=0, error=0)
        destinations = set()
        for name, file_id in files.items():
            try:
                valid_name(name)
                dest = classify_destination(name, target) / name
                if dest in destinations:
                    raise ValueError('Nhiều file nguồn trùng đích')
                destinations.add(dest)
                status, metadata = sync_one(name, file_id, dest, manifest.get(file_id), incoming, ROOT)
                if metadata:
                    manifest[file_id] = metadata
                    atomic_json(manifest_path, manifest)
                counts[status] += 1
                print(f'{status}: {name}')
            except Exception as exc:
                counts['error'] += 1
                print(f'error: {name}: {exc}', file=sys.stderr)
        print('Kết quả các file nhận diện được: ' + ', '.join(f'{k}={v}' for k, v in counts.items()))
        return 1 if counts['error'] else (2 if counts['conflict'] else 0)
    except Exception as exc:
        print(f'Dừng đồng bộ: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
