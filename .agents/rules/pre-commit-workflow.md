# Kiểm tra, commit và push

Áp dụng [quy tắc nguồn dữ liệu](./source-of-truth.md) trước khi thay đổi nội dung.

## Hoàn thành chỉnh sửa

1. Xem `git status --short` và diff, phân biệt thay đổi đang có của người dùng với thay đổi mới.
2. Kiểm tra nội dung theo nguồn, liên kết và ảnh. Với Markdown/HTML cùng tài liệu, đối chiếu nội dung và mở HTML để kiểm tra hiển thị khi thay đổi bố cục.
3. Cập nhật timeline khi có tiến độ thực tế hoặc điều chỉnh kế hoạch. Không bắt buộc đổi timeline vì sửa lỗi chính tả hoặc công cụ. Cập nhật `.agents/README.md` khi đổi cách dùng skills/scripts.
4. Chạy kiểm tra phù hợp rồi báo file đã sửa, kết quả kiểm tra và phần chưa xác minh. Kết thúc đầu việc không tự cấp quyền commit/push.

## Khi được yêu cầu commit hoặc push

- Yêu cầu commit cho phép stage và commit phần việc liên quan. Yêu cầu push bao gồm tạo commit cần thiết cho phần việc đang trao đổi, trừ khi người dùng giới hạn khác. Quyền cho một lần push không tự áp dụng cho các đầu việc mới.
- Kiểm tra nhánh, remote và staged diff. Stage theo phạm vi, không tự đưa thay đổi không liên quan vào commit.
- Chạy `git diff --cached --check` và `bash .agents/scripts/pre_commit_check.sh`.
- Dùng Conventional Commits, mô tả kết quả cụ thể. Không tự bỏ qua hook.
- Chỉ push khi được yêu cầu. Không tự force-push. Nếu remote đi trước, fetch và đánh giá diff trước khi tích hợp, giữ các thay đổi local.
- Xác nhận kết quả push từ Git, báo nhánh và commit. Không báo đã push chỉ vì đã commit.
