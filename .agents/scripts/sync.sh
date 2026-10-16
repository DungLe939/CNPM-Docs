#!/usr/bin/env bash
# .agents/scripts/sync.sh
# Lệnh tắt 1 dòng dành cho các thành viên trong nhóm để:
# 1. Kéo commit mới nhất từ GitHub về (git pull origin)
# 2. Tải các tài liệu/biên bản họp mới nhất từ Google Drive về repo (mặc định vào docs/Week01/)

set -e
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

python3 .agents/scripts/sync_drive.py --pull "$@"
