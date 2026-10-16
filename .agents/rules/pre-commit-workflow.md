# Quy trình Bắt buộc Trước khi Commit (Pre-Commit Finalization Workflow)

Tài liệu này là quy tắc ứng xử (Rule) bắt buộc dành cho AI khi hỗ trợ dự án **Nhập môn Công nghệ Phần mềm**.

---

## 1. Nguyên tắc Kích hoạt (Trigger)

Mỗi khi người dùng đưa ra các yêu cầu liên quan đến:
- *"commit giúp tôi"*, *"tạo git commit"*, *"commit code/docs"*
- *"push lên git"*, *"kết thúc buổi làm việc"*
- Hoặc hoàn tất một đầu việc lớn trong tuần.

**AI KHÔNG ĐƯỢC CHẠY LỆNH `git commit` NGAY LẬP TỨC.**  
AI **BẮT BUỘC** phải tự động rà soát và thực hiện quy trình **Finalize Checklist** dưới đây trước khi commit.

---

## 2. Checklist Finalize Tự Động Trước Khi Commit

### Bước 0: Nắm bắt Toàn cảnh Thay đổi
- Chạy `git status` và `git diff --stat` để liệt kê **toàn bộ** các file đã thay đổi, thêm mới hoặc xóa.
- Dựa vào kết quả để xác định bước nào bên dưới cần thực hiện (không phải lúc nào cũng cần chạy hết).

### Bước 1: Rà soát & Cập nhật Tiến độ (`WEEKLY_TIMELINE.md`)
- **Điều kiện:** Có file thay đổi trong `docs/` hoặc mã nguồn liên quan đến đồ án.
- Mở file [docs/WEEKLY_TIMELINE.md](../docs/WEEKLY_TIMELINE.md):
  - Cập nhật trạng thái tuần hiện tại (ví dụ: `Đang thực hiện` ➔ `Đã hoàn thành`).
  - Ghi nhận liên kết tương đối đến các tài liệu, artifact vừa tạo.

### Bước 2: Đồng bộ Danh mục Kỹ năng & Bản đồ Thư mục
- **Điều kiện:** Có file thay đổi trong `.agents/skills/`, `.agents/rules/`, hoặc `.agents/scripts/`.
- Nếu có skill/rule/script **thêm mới, đổi tên hoặc cập nhật chức năng chính**:
  - Cập nhật bảng tổng quan trong [.agents/README.md](../README.md).
  - Cập nhật bản đồ thư mục trong [project-navigator/SKILL.md](../skills/project-navigator/SKILL.md) nếu cấu trúc thư mục thay đổi (thêm/xóa folder, file quan trọng).

### Bước 3: Kiểm duyệt Chất lượng Văn bản & Đường dẫn
- **Đường dẫn tương đối (Relative paths):** Quét qua các file `.md` vừa sửa, đảm bảo KHÔNG chứa đường dẫn tuyệt đối dạng `/Users/...`, `C:\...` hay `C:/...`. Tất cả phải dùng `./` hoặc `../`.
- **Loại bỏ AI Fluff:** Nếu có tài liệu kỹ thuật/báo cáo đồ án được soạn thảo, kích hoạt skill [anti-ai-fluff](../skills/anti-ai-fluff/SKILL.md) để rà soát từ ngữ sáo rỗng, hoa mỹ trước khi lưu.

### Bước 4: Tạo Commit Thông Minh
- Sau khi docs và skills đã được đồng bộ đầy đủ, AI mới tiến hành `git add` và `git commit`.
- Commit message phải rõ ràng, tuân thủ Conventional Commits:
  - `docs(weekXX): finalize báo cáo và cập nhật timeline tuần XX`
  - `feat(skills): thêm skill xyz và cập nhật catalog`
  - `fix(docs): sửa liên kết tương đối trong tài liệu`
  - `chore(agents): cập nhật rules pre-commit workflow`

---

## 3. Lưu ý Quan trọng

- **Không bỏ bước:** Ngay cả khi người dùng nói *"commit nhanh đi"*, AI vẫn phải chạy ít nhất Bước 0 và Bước 3 (kiểm duyệt đường dẫn).
- **Có thể bỏ qua thủ công:** Nếu người dùng nói rõ *"commit --no-verify"* hoặc *"bỏ qua kiểm tra"*, AI được phép bỏ qua checklist.
- **Không tự ý push:** AI chỉ `commit`, không tự ý `git push` trừ khi người dùng yêu cầu rõ ràng.
