---
name: se-proposal-writer
description: >-
  Kích hoạt khi người dùng yêu cầu soạn thảo, chỉnh sửa hoặc hoàn thiện tài liệu
  Project Proposal (Đề xuất đồ án đợt 1) theo biểu mẫu của bộ môn CNPM.
---

# SE PROPOSAL WRITER: SOẠN THẢO PROJECT PROPOSAL CHUẨN

Skill này hướng dẫn AI viết tài liệu **Project Proposal** bám sát 100% biểu mẫu `Template#0-ProjectProposal-2022.docx` của Khoa CNTT - ĐH KHTN TP.HCM.

---

## 1. Cấu trúc Bắt buộc theo Biểu mẫu Bộ môn

Tài liệu Proposal hoàn chỉnh **phải có đầy đủ 5 phần** sau:

### Phần Đầu: Bảng Đánh giá Thành viên
Bắt buộc có bảng theo mẫu:
```markdown
| MSSV | Họ Tên | Vai trò chính | % Đóng góp (Tối đa 100%) | Chữ ký |
| :---: | :--- | :--- | :---: | :---: |
| <MSSV1> | <Họ tên 1> | Trưởng nhóm / Fullstack | 100% | *(Ký khi nộp)* |
| <MSSV2> | <Họ tên 2> | Frontend Developer | 100% | *(Ký khi nộp)* |
| <MSSV3> | <Họ tên 3> | Backend Developer | 100% | *(Ký khi nộp)* |
| <MSSV4> | <Họ tên 4> | Tester / QA | 100% | *(Ký khi nộp)* |
```

---

### Mục 1: Phát biểu Bài toán Sơ lược (Khoảng 1 - 2 trang)
- **Bối cảnh & Nghiệp vụ cốt lõi:** Mô tả ngắn gọn vấn đề thực tế mà phần mềm giải quyết.
- **Môi trường hoạt động:** 
  - Phía Client: Trình duyệt hỗ trợ HTML5/CSS3 (Chrome, Safari, Edge), thiết bị di động (nếu có).
  - Phía Server: Node.js/Python/Java, Web server (Nginx/Apache), Điện toán đám mây (AWS/Vercel/Render).
- **Ràng buộc thiết kế & triển khai:**
  - Ngôn ngữ & Framework (ví dụ: Next.js/React, Express.js/FastAPI).
  - Hệ quản trị cơ sở dữ liệu (PostgreSQL/MySQL/MongoDB).
  - Chuẩn mã nguồn và tài liệu (ESLint, Git flow, tài liệu Markdown).
- ⚠️ **LƯU Ý:** Chỉ dừng ở mức độ **sơ lược**. Tuyệt đối không vẽ Sequence Diagram hay đặc tả chi tiết Use Case ở đây (sẽ làm ở tài liệu Phân tích).

---

### Mục 2: Giải pháp Đề xuất

#### 2.1. Phần mềm
- **Danh sách chức năng (User Stories):** Lập bảng câu chuyện người dùng để lý giải sự cần thiết của từng chức năng:
  ```markdown
  | ID | Vai trò (As a...) | Mong muốn (I want to...) | Lợi ích (So that...) | Tiêu chí chấp nhận (Acceptance Criteria) |
  | :---: | :--- | :--- | :--- | :--- |
  | US-01 | Khách vãng lai | Tìm kiếm sản phẩm theo tên | Nhanh chóng tìm được món hàng ưng ý | Trả về danh sách kết quả phù hợp trong < 1s |
  ```
- **Kiến trúc tổng thể phần mềm:** Mô tả kiến trúc mức cao (High-level Architecture), ví dụ mô hình Client-Server 3 lớp (Presentation - Application/API - Data Layer) kèm sơ đồ Mermaid trực quan.

#### 2.2. Phần cứng & Hạ tầng
- Cấu hình máy chủ tối thiểu (CPU, RAM, Storage).
- Yêu cầu thiết bị người dùng cuối (smartphone, smartwatch hoặc PC thông thường).

---

### Mục 3: Kế hoạch Phát triển Phần mềm
Lựa chọn mô hình phát triển rõ ràng (**Scrum** hoặc **Waterfall**):
- Liệt kê các giai đoạn và thành phẩm đầu ra cụ thể:
  1. Phân tích yêu cầu (Requirements Analysis) $\rightarrow$ SRS document
  2. Thiết kế phần mềm (Software Design) $\rightarrow$ Architecture & DB Schema
  3. Cài đặt (Implementation) $\rightarrow$ Mã nguồn trên GitHub
  4. Kiểm thử phần mềm (Testing) $\rightarrow$ Test Plan & Test Cases
  5. Triển khai & Bảo trì (Deployment & Maintenance) $\rightarrow$ Link Web / App chạy thực tế

---

### Mục 4: Kế hoạch Nhân sự & Chi phí
- **Cấu trúc nhân sự:** Phân chia trách nhiệm (RACI matrix hoặc mô hình Scrum: Product Owner, Scrum Master, Developers, QA).
- **Chi phí dự kiến:** 
  - Hạ tầng / Hosting: Tận dụng Free Tier (Vercel, Supabase, Neon) hoặc ước tính chi phí cụ thể.
  - Tên miền, API bên thứ ba (nếu có).

---

## 2. Tiêu chuẩn Kiểm duyệt Chất lượng

Trước khi bàn giao bản Proposal cho người dùng, AI phải tự kiểm tra:

- [ ] Đã đủ 5 phần chính (Bảng thành viên + 4 mục nội dung) chưa?
- [ ] Dung lượng phát biểu bài toán có vượt quá 2 trang không?
- [ ] Bảng User Story có đúng định dạng chuẩn (As a... I want to... So that...) không?
- [ ] Đã kích hoạt skill `anti-ai-fluff` để lọc sạch từ ngữ sáo rỗng chưa?
- [ ] Tất cả liên kết trong tài liệu đều dùng đường dẫn tương đối (relative path) chưa?
