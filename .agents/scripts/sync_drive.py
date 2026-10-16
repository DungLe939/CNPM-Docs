#!/usr/bin/env python3
"""
scripts/sync_drive.py
---------------------
Công cụ tự động đồng bộ tài liệu từ Google Drive của nhóm về repository.
Mặc định đồng bộ về: docs/Drive_Sync/

Cách dùng:
    python3 scripts/sync_drive.py          # Tự động quét và tải file mới
    python3 scripts/sync_drive.py --pull   # Chạy git pull origin trước rồi mới sync Drive
    python3 scripts/sync_drive.py --force  # Tải lại toàn bộ file bất kể đã tồn tại
"""

import sys
import os
import re
import json
import argparse
import subprocess
import urllib.request
import urllib.error
import hashlib
from datetime import datetime

DEFAULT_FOLDER_ID = "12e0__KnGQOQayRmNEWwYPrq-0ErlqGph"
DEFAULT_TARGET_DIR = os.path.join("docs", "Week01")
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# ANSI Colors for terminal output
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def run_git_pull():
    """Tự động kéo commit mới nhất từ origin về trước khi đồng bộ."""
    print(f"{BLUE}[1/2] Đang kiểm tra và đồng bộ Git từ GitHub (git pull origin)...{RESET}")
    try:
        # Lấy tên branch hiện tại
        branch_res = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, check=True
        )
        current_branch = branch_res.stdout.strip() or "main"
        
        pull_res = subprocess.run(
            ["git", "pull", "origin", current_branch],
            capture_output=True, text=True, check=True
        )
        print(f"{GREEN}✓ Git Pull thành công (Branch: {current_branch}):{RESET}")
        for line in pull_res.stdout.strip().split("\n"):
            print(f"  {line}")
    except subprocess.CalledProcessError as e:
        print(f"{YELLOW}⚠ Cảnh báo: git pull gặp vấn đề ({e.stderr.strip()}). Tiếp tục đồng bộ Drive...{RESET}")
    except Exception as e:
        print(f"{YELLOW}⚠ Không thể thực hiện git pull: {e}. Tiếp tục đồng bộ Drive...{RESET}")


def fetch_folder_html(folder_id):
    """Lấy nội dung HTML của thư mục Google Drive."""
    url = f"https://drive.google.com/drive/folders/{folder_id}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            return response.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"{RED}✗ Lỗi khi truy cập Google Drive: {e}{RESET}")
        return None


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


def download_file(file_name, file_id, dest_path):
    """Tải file từ Google Drive và lưu vào dest_path."""
    # Thử tải trực tiếp từ direct download endpoint
    direct_url = f"https://drive.usercontent.google.com/download?id={file_id}&export=download"
    req = urllib.request.Request(direct_url, headers={"User-Agent": USER_AGENT})

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read()
            # Kiểm tra xem nội dung tải về có phải là trang HTML báo lỗi không
            if len(content) < 1000 and b"<!DOCTYPE html>" in content and b"ServiceLogin" in content:
                raise ValueError("Cần đăng nhập hoặc không có quyền truy cập trực tiếp")
            
            with open(dest_path, "wb") as f:
                f.write(content)
            return True, len(content)
    except Exception:
        # Nếu là Google Doc nội bộ (gdoc), thử export qua endpoint docs.google.com
        ext = os.path.splitext(file_name)[1].lower()
        export_format = "txt"
        if ext == ".docx":
            export_format = "docx"
        elif ext == ".pdf":
            export_format = "pdf"
        elif ext == ".html":
            export_format = "html"

        export_url = f"https://docs.google.com/document/d/{file_id}/export?format={export_format}"
        req_exp = urllib.request.Request(export_url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req_exp, timeout=30) as resp:
                content = resp.read()
                with open(dest_path, "wb") as f:
                    f.write(content)
                return True, len(content)
        except Exception as e2:
            return False, str(e2)


def load_manifest(manifest_path):
    """Đọc file lưu vết manifest."""
    if os.path.exists(manifest_path):
        try:
            with open(manifest_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_manifest(manifest_path, manifest):
    """Lưu manifest để theo dõi các file đã đồng bộ."""
    try:
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"{YELLOW}⚠ Không thể lưu manifest: {e}{RESET}")


def get_file_hash(filepath):
    """Tính SHA256 để kiểm tra trùng lặp."""
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()


def classify_destination(file_name, target_week_dir):
    """
    Tự động phân loại file vào đúng thư mục con:
    1. Team Decision:
       - Biên bản họp (meeting, bien_ban) -> docs/WeekXX/Team_Decision/
       - Kế hoạch triển khai, tài liệu nhóm (plan, proposal, jobseeker, decision)
         -> docs/WeekXX/Team_Decision/Material/
    2. Tài liệu học tập, đồ án, thông báo từ Thầy (material, thong_bao, template)
       -> docs/WeekXX/Material/
    3. Bài toán mẫu, đề bài (problem, example)
       -> docs/WeekXX/Problem_example/
    4. Mặc định -> target_week_dir
    """
    name_lower = file_name.lower()

    # 1. Biên bản họp của nhóm -> Team_Decision
    if any(k in name_lower for k in ["meeting", "bien_ban", "hop_nhom"]):
        return os.path.join(target_week_dir, "Team_Decision")

    # 2. Tài liệu, kế hoạch triển khai do nhóm tự làm -> Team_Decision/Material
    if any(k in name_lower for k in ["jobseeker", "plan", "proposal", "decision"]):
        return os.path.join(target_week_dir, "Team_Decision", "Material")

    # 3. Tài liệu, đồ án yêu cầu của Thầy -> Material
    if any(k in name_lower for k in ["material", "thong_bao", "template", "tai_lieu", "slide", "guide", "huong_dan"]):
        return os.path.join(target_week_dir, "Material")

    # 4. Bài toán mẫu, đề bài
    if any(k in name_lower for k in ["problem", "example", "bai_toan", "de_bai"]):
        return os.path.join(target_week_dir, "Problem_example")

    return target_week_dir


def main():
    parser = argparse.ArgumentParser(description="Đồng bộ tài liệu từ Google Drive của nhóm đồ án.")
    parser.add_argument("--folder", default=DEFAULT_FOLDER_ID, help="Google Drive Folder ID")
    parser.add_argument("--target", default=None, help="Thư mục đích lưu file trong repo (mặc định theo tuần)")
    parser.add_argument("--week", default="Week01", help="Tên tuần muốn tổng hợp tài liệu (ví dụ: Week01, Week02, ...)")
    parser.add_argument("--pull", action="store_true", help="Chạy git pull origin trước khi sync Drive")
    parser.add_argument("--force", action="store_true", help="Bắt buộc tải lại toàn bộ file")
    args = parser.parse_args()

    if not args.target:
        args.target = os.path.join("docs", args.week)

    print(f"\n{BOLD}{CYAN}=== CÔNG CỤ ĐỒNG BỘ GOOGLE DRIVE (CNPM DOCS) ==={RESET}")
    print(f"Folder ID : {args.folder}")
    print(f"Lưu vào   : {args.target} (tự động phân loại subfolder)")
    print("-" * 50)

    # 1. Chạy git pull nếu được yêu cầu
    if args.pull:
        run_git_pull()
        print("-" * 50)

    # 2. Quản lý manifest lưu vết bên trong thư mục scripts (không gây rác thư mục docs)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    manifest_path = os.path.join(script_dir, ".sync_manifest.json")
    manifest = load_manifest(manifest_path)

    # 3. Quét danh sách file trên Google Drive
    step_label = "[2/2]" if args.pull else "[1/1]"
    print(f"{BLUE}{step_label} Đang quét danh sách file trên Google Drive...{RESET}")
    html = fetch_folder_html(args.folder)
    if not html:
        print(f"{RED}Không thể lấy dữ liệu từ Google Drive. Vui lòng kiểm tra kết nối mạng.{RESET}")
        sys.exit(1)

    files = extract_files_from_html(html)
    if not files:
        print(f"{YELLOW}Không tìm thấy file nào hoặc quyền truy cập folder chưa được mở công khai.{RESET}")
        sys.exit(0)

    print(f"{GREEN}✓ Tìm thấy {len(files)} file trên Google Drive:{RESET}")
    for name, fid in files.items():
        print(f"  • {name} (ID: {fid})")

    print("-" * 50)
    print(f"{BLUE}Bắt đầu phân loại và đồng bộ vào '{args.target}'...{RESET}\n")

    synced_count = 0
    skipped_count = 0
    error_count = 0
    updated_files = []

    for name, fid in files.items():
        # Phân loại tự động vào thư mục con phù hợp
        dest_dir = classify_destination(name, args.target)
        os.makedirs(dest_dir, exist_ok=True)
        dest_path = os.path.join(dest_dir, name)
        rel_dest = os.path.relpath(dest_path, ".")

        file_info = manifest.get(fid, {})

        # Kiểm tra xem file đã có sẵn chưa
        if os.path.exists(dest_path) and not args.force:
            current_hash = get_file_hash(dest_path)
            if file_info.get("hash") == current_hash and file_info.get("name") == name:
                print(f"  {YELLOW}⏩ Đã có (Bỏ qua):{RESET} {name} -> {rel_dest}")
                skipped_count += 1
                continue

        # Tiến hành tải
        print(f"  {CYAN}⬇ Đang tải:{RESET} {name} -> {rel_dest} ...", end=" ", flush=True)
        success, res = download_file(name, fid, dest_path)
        if success:
            file_hash = get_file_hash(dest_path)
            manifest[fid] = {
                "name": name,
                "file_id": fid,
                "size_bytes": res,
                "hash": file_hash,
                "dest_path": rel_dest,
                "synced_at": datetime.now().isoformat()
            }
            print(f"{GREEN}Xong ({res:,} bytes){RESET}")
            synced_count += 1
            updated_files.append((name, rel_dest))
        else:
            print(f"{RED}Thất bại ({res}){RESET}")
            error_count += 1

    # Lưu lại manifest vào .agents/scripts/.sync_manifest.json
    save_manifest(manifest_path, manifest)

    print("\n" + "=" * 50)
    print(f"{BOLD}KẾT QUẢ ĐỒNG BỘ:{RESET}")
    print(f"  • Mới/Cập nhật: {GREEN}{synced_count}{RESET} file")
    print(f"  • Đã có sẵn   : {YELLOW}{skipped_count}{RESET} file")
    if error_count > 0:
        print(f"  • Lỗi         : {RED}{error_count}{RESET} file")
    print("=" * 50)

    if updated_files:
        print(f"\n{GREEN}{BOLD}Các file mới đã được phân loại vào đúng thư mục:{RESET}")
        for f_name, f_path in updated_files:
            print(f"  - [{f_name}]({f_path})")
    else:
        print(f"\n{CYAN}Tất cả tài liệu đều đã ở phiên bản mới nhất!{RESET}")


if __name__ == "__main__":
    main()
