---
name: project-utility
description: >-
  Kỹ năng đa năng (utility) cung cấp các quy tắc chung về liên kết đường dẫn tương đối,
  chuẩn hóa đặt tên file, xử lý tài liệu Markdown, và các tiện ích vận hành đồ án.
---

# PROJECT UTILITY: QUY TẮC CHUNG & TIỆN ÍCH DỰ ÁN

Skill này đóng vai trò là cẩm nang tiện ích và chuẩn mực thao tác chung cho mọi tác vụ trong đồ án môn học.

---

## 🌟 1. Quy tắc Vàng về Đường dẫn (Path Rule)

> **"Nếu được, hãy sử dụng đường dẫn tương đối (relative path) nhiều nhất có thể."**

- **Lý do:** Dự án được làm việc theo nhóm và đẩy lên GitHub. Đường dẫn tuyệt đối (`file:///Users/...` hoặc `C:\...`) sẽ lập tức bị lỗi khi đồng đội hoặc giảng viên mở trên máy khác.
- **Quy tắc thực hành:**
  - Trong tài liệu Markdown, luôn dùng relative link: `[text1.md](./Week01/text1.md)`, `[Template](../Template#0-ProjectProposal-2022.pdf)`.
  - Trong mã nguồn / script: Luôn sử dụng đường dẫn tương đối tính từ thư mục chạy hoặc vị trí file script hiện tại.
  - Tuyệt đối không hardcode thư mục cá nhân người dùng.

---

## 2. Quy ước Đặt tên File & Thư mục (Naming Conventions)

- **Thư mục tiến độ:** Luôn đặt theo định dạng `Week<XX>` (ví dụ: `Week01`, `Week02`, `Week03`).
- **File tài liệu chính thức:** Đặt tên rõ ràng, viết bằng tiếng Anh hoặc tiếng Việt không dấu:
  - PascalCase hoặc kebab-case: `Project_Proposal.md`, `Software_Specification.md`, `team-decision-01.md`.
- **File dữ liệu thô:** Luôn kèm hậu tố `_raw.md` để phân biệt với tài liệu đã chuẩn hóa.
- **Tránh ký tự đặc biệt:** Không đặt tên file chứa khoảng trắng vô nghĩa hoặc ký tự có dấu tiếng Việt trên hệ thống file để tránh lỗi khi sync Git.

---

## 3. Tiêu chuẩn Trình bày Markdown & Bảng biểu

- **Tiêu đề phân cấp:** Sử dụng đúng thứ tự `h1 (#)` $\rightarrow$ `h2 (##)` $\rightarrow$ `h3 (###)`, không nhảy cóc cấp độ.
- **Bảng biểu (GFM Tables):**
  - Luôn có dòng tiêu đề và phân cách viền (`| :--- | :---: |`).
  - Dữ liệu chữ căn trái (`:---`), số liệu / ngày tháng / trạng thái căn giữa (`:---:`).
- **Trích dẫn & Ghi chú:** Dùng blockquote `>` hoặc alert blocks để làm nổi bật lưu ý quan trọng từ giảng viên.

---

## 4. Tự động Đồng bộ Ngữ cảnh (Sync Context)

Khi tạo mới một bài nộp hoặc hoàn thành một mốc công việc:
1. Kiểm tra và cập nhật trạng thái tương ứng trong file `docs/WEEKLY_TIMELINE.md`.
2. Đảm bảo file mới được tham chiếu bằng đường dẫn tương đối từ tài liệu tuần hoặc tài liệu tổng quan.
