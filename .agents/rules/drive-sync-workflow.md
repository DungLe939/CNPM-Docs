# Đồng bộ Git và Google Drive

Áp dụng khi người dùng yêu cầu lấy tài liệu từ Drive. Đọc [quy tắc nguồn dữ liệu](./source-of-truth.md). Không nhắc hỏi đồng bộ ở mọi phiên đọc tài liệu local.

## Thực hiện

1. Xem trạng thái Git và nhánh hiện tại. Khi cần cập nhật Git, chỉ pull fast-forward với working tree sạch. Không tự stash/rebase hay che lỗi. Pull lỗi thì dừng luồng đồng bộ có pull.
2. Dùng script trong [drive-sync](../skills/drive-sync/SKILL.md). Tải dữ liệu vào file tạm, so sánh nội dung local, remote và hash lần đồng bộ trước rồi mới thay thế.
3. File local đã sửa, file có sẵn chưa có baseline, file bị xóa/di chuyển local hoặc file trong `Submission/` cần được bảo vệ. Giữ bản tải khác biệt trong `.agents/scripts/.sync_incoming/` để đối chiếu, không ghi đè. Không tự xóa tài liệu theo trạng thái Drive.
4. Nếu bản local và remote giống nhau, có thể ghi nhận baseline. Chỉ cập nhật tự động khi local vẫn bằng baseline và remote có thay đổi. Kiểm tra thay đổi local lần nữa ngay trước khi ghi.
5. Báo riêng file cập nhật, không đổi, xung đột và lỗi. Không khẳng định đã lấy toàn bộ Drive: bộ đọc hiện tại chỉ xử lý các file mà nó nhận diện trong trang thư mục công khai.

## Sau đồng bộ

Tóm tắt thay đổi có nguồn trong chat, không tự tạo báo cáo. File tải về không tự trở thành nguồn chuẩn. Không suy ra sự kiện họp từ tên file hay lịch dự kiến. Chỉ dẫn link Drive gốc khi thực sự có ID của nguồn, không sao chép ID ví dụ.

Cache và bản tải chờ đối chiếu nằm trong `.agents/scripts/`, được Git bỏ qua. Không đưa chúng vào hồ sơ nộp.
