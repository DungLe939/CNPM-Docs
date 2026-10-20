---
name: drive-sync
description: Lấy và đối chiếu tài liệu Google Drive khi người dùng yêu cầu đồng bộ hoặc lấy tài liệu mới, bảo vệ các chỉnh sửa local.
---

# Đồng bộ Drive

Đọc [quy trình đồng bộ](../../rules/drive-sync-workflow.md) và [quy tắc nguồn dữ liệu](../../rules/source-of-truth.md). Không kích hoạt chỉ vì người dùng muốn đọc tài liệu local.

## Sử dụng

Từ thư mục gốc dự án:

```bash
# Cập nhật Git fast-forward rồi đối chiếu Drive (yêu cầu working tree sạch)
./.agents/scripts/sync.sh --week Week01

# Chỉ lấy Drive nếu người dùng yêu cầu như vậy, không tự pull Git
python3 .agents/scripts/sync_drive.py --week Week01
```

`--week` chọn tuần theo yêu cầu thực tế, mặc định Week01 để tương thích. `--folder` chọn ID thư mục nguồn. `--target` chọn thư mục đích bên trong dự án. `--force` không còn được hỗ trợ vì có thể ghi đè nội dung đã kiểm tra.

Script dùng thư viện chuẩn Python, đọc trang thư mục Drive công khai. Nếu cần đăng nhập hoặc không nhận diện được danh sách, báo giới hạn và dừng, không đổi quyền chia sẻ của người dùng. Không bảo đảm nhận diện thư mục con hay mọi định dạng Google Docs.

Mỗi lần chạy tải bản remote để so sánh, không dựa vào hash local để kết luận remote chưa đổi. Xung đột giữ ở `.agents/scripts/.sync_incoming/`, không ghi đè bản local. Báo file thay đổi, không đổi, xung đột và lỗi. Đối chiếu bản incoming trước khi người dùng quyết định cách hợp nhất, không tự coi bản Drive là nguồn chuẩn.
