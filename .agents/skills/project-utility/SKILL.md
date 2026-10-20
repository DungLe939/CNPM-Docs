---
name: project-utility
description: Chuẩn hóa đường dẫn, tài nguyên và bản Markdown/HTML khi chỉnh tài liệu dự án.
---

# Tiện ích tài liệu

Áp dụng [quy tắc nguồn dữ liệu](../../rules/source-of-truth.md).

- Liên kết nội bộ dùng đường dẫn tương đối tính từ file chứa link. Mã hóa `#` trong tên file thành `%23`. Giữ nguyên tên file hiện có trừ khi cần đổi, cập nhật mọi tham chiếu khi đổi tên.
- File mới đặt theo tuần và mục đích thực tế. Không dời file đã duyệt chỉ để khớp sơ đồ thư mục cũ.
- Nếu có nguồn cloud xác định, dẫn cả bản local và link nguồn khi hữu ích. Không bịa link Drive hoặc dùng ID ví dụ.
- Sửa nội dung chung thì đồng bộ Markdown/HTML. Phân biệt thay đổi nội dung với CSS, kiểm tra ảnh, bảng và sơ đồ. Nếu chưa có renderer chung, giữ bố cục hiện có và đối chiếu hai bản, không tự thiết kế lại.
- Đóng ZIP phải giữ cấu trúc các ảnh và tài nguyên local được tham chiếu. Tên ZIP và cách nộp theo yêu cầu có nguồn.
- Dùng `python3 .agents/scripts/check_docs.py` để kiểm tra file đang làm việc, hoặc `--staged` để kiểm tra nội dung trong Git index. Công cụ kiểm tra link và cảnh báo chênh lệch, không chứng minh dữ kiện đúng hay giao diện hiển thị đúng.
- Timeline chỉ ghi thay đổi kế hoạch hoặc tiến độ có căn cứ. Khi commit, theo [quy trình commit](../../rules/pre-commit-workflow.md).
