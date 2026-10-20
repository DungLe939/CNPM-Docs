# Hướng dẫn và công cụ cho agent

Bắt đầu bằng [quy tắc nguồn dữ liệu](./rules/source-of-truth.md). Skills giúp thực hiện tác vụ, không xác nhận dữ kiện của dự án. Chỉ dẫn của người dùng xác định phạm vi công việc, đọc tài liệu không tự cho phép sync hoặc commit.

## Skills

| Skill | Dùng khi |
| :--- | :--- |
| [project-navigator](./skills/project-navigator/SKILL.md) | Tra cứu cấu trúc, nguồn và tiến độ |
| [se-proposal-writer](./skills/se-proposal-writer/SKILL.md) | Soạn/chỉnh Proposal theo nguồn đã xác nhận |
| [anti-ai-fluff](./skills/anti-ai-fluff/SKILL.md) | Biên tập văn phong, giữ nguyên dữ kiện |
| [project-utility](./skills/project-utility/SKILL.md) | Kiểm tra liên kết, tài nguyên và Markdown/HTML |
| [drive-sync](./skills/drive-sync/SKILL.md) | Lấy tài liệu Drive khi được yêu cầu |

## Quy trình

Đọc yêu cầu → xác định nguồn → kiểm tra hiện trạng → sửa đúng phạm vi → kiểm tra nội dung/hiển thị → báo kết quả → commit/push theo yêu cầu.

- [Nguồn dữ liệu](./rules/source-of-truth.md): phân biệt nguồn chuẩn, ghi chép gốc, kế hoạch và kết quả thực tế.
- [Đồng bộ Drive](./rules/drive-sync-workflow.md): bảo vệ bản local, xử lý xung đột, dừng khi pull lỗi.
- [Commit/push](./rules/pre-commit-workflow.md): tách việc kiểm tra khỏi quyền tạo commit và đẩy GitHub.

## Công cụ

- `./.agents/scripts/sync.sh --week Week01`: cập nhật Git fast-forward và đối chiếu Drive. Chỉ chạy khi cần đồng bộ.
- `python3 .agents/scripts/check_docs.py`: kiểm tra tài liệu trong working tree. Thêm `--staged` để kiểm tra Git index.
- `bash .agents/scripts/pre_commit_check.sh`: kiểm tra staged diff và tài liệu trước commit.
- `python3 -m unittest discover -s .agents/scripts/tests -v`: kiểm thử offline cho sync và kiểm tra tài liệu, không gọi Drive/GitHub thật.

Hook `.git/hooks/pre-commit` hiện có gọi script kiểm tra, nhưng hook nằm ngoài file được Git theo dõi nên clone mới không tự có hook. Có thể chạy script thủ công trước commit.

Kiểm tra tài liệu chặn link/ảnh local bị thiếu và đường dẫn tuyệt đối trong tài liệu được kiểm tra. Khi xóa tài nguyên, kiểm tra các tài liệu còn lại để phát hiện tham chiếu hỏng. Chênh lệch Markdown/HTML chỉ là cảnh báo cần đối chiếu, không phải phép xác minh toàn bộ nội dung hoặc layout. Công cụ không xác nhận tính đúng của dữ kiện.

Cache `.sync_manifest.json` và `.sync_incoming/` được Git bỏ qua. VS Code chỉ auto-fetch để biết cập nhật remote, không tự pull khi mở thư mục.
