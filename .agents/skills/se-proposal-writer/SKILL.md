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
Lựa chọn mô hình phát triển rõ ràng (**Scrum (Agile)** theo chu kỳ Sprint hoặc **Waterfall**), quản lý trên nền tảng quản trị công việc (như Jira Software):
- Nếu áp dụng Scrum, chia lộ trình thành các Sprint cố định (ví dụ 2 tuần / Sprint).
- Mỗi Sprint tập trung thể hiện trực quan và rõ ràng 3 thành phần cốt lõi:
  1. **Mục tiêu Sprint (Sprint Goal):** Nêu rõ giá trị nghiệp vụ hoặc khả năng mới mà hệ thống đạt được sau Sprint bằng ngôn ngữ dễ hiểu.
  2. **Kế hoạch cụ thể theo từng tuần:** Nêu rõ công việc trọng tâm từng tuần, bám sát nghiệp vụ thực tế, người mới đọc vào hiểu ngay cần làm gì.
  3. **Thành phẩm cụ thể đầu ra (Deliverables):** Mô tả rõ bản chất và nội dung cốt lõi của sản phẩm (tài liệu, bản thiết kế giao diện, module phần mềm, báo cáo kiểm thử).
- Bảng tổng hợp lộ trình phát triển tập trung vào tiến độ các tuần và thành phẩm có thể kiểm chứng được (Deliverables). Ước lượng công số (Man-Hours) không để rải rác trong từng Sprint mà được gom quản lý tập trung ở mục Kế hoạch Nhân sự & Chi phí để tránh làm loãng bức tranh phát triển kỹ thuật.

#### ⚠️ QUY TẮC CỐT LÕI: DIỄN ĐẠT TRỰC QUAN & THÂN THIỆN CHO NGƯỜI NGOÀI NGÀNH (NON-TECH & ONBOARDING-FRIENDLY)
1. **Không liệt kê tên file cộc lốc (No Raw Filename Drops):**
   - Tuyệt đối không chỉ ghi tên tệp mã nguồn hoặc tài liệu (ví dụ: `Project_Proposal.md`, `SRS.md`, `Meeting_01.md`, `Test_Report.md`...) như một đầu mục thành phẩm mà không có lời giải thích.
   - Giảng viên, người chấm điểm hoặc các bên liên quan phi kỹ thuật (non-tech) sẽ không hiểu một tên file viết tắt có ý nghĩa gì và chứa nội dung gì.
   - **Phải mô tả bản chất thành phẩm:** Nêu rõ tên sản phẩm nghiệp vụ, giải thích tóm tắt nội dung chính và giá trị thực tế của nó (nếu có tên file kỹ thuật thì để trong ngoặc kèm link tham chiếu, nhưng phần mô tả nghiệp vụ phải đứng trước và là trọng tâm).
   - *Ví dụ sai:* `* Hồ sơ đề xuất đồ án: Project_Proposal.md và Project_Proposal.html.`
   - *Ví dụ chuẩn:* `* Bộ hồ sơ đề xuất đồ án (Project Proposal): Tài liệu toàn diện trình bày bối cảnh bài toán tuyển dụng, khảo sát khó khăn của sinh viên IT, giải pháp 5 phân hệ công nghệ, kiến trúc kỹ thuật Client - Server và kế hoạch 4 Sprint (8 tuần) kèm phân bổ nhân sự.`
2. **Ngôn từ trực quan, người mới tham gia dự án đọc vào hiểu ngay:**
   - Tránh dùng từ lóng kỹ thuật nội bộ hoặc viết tắt bí hiểm khi mô tả công việc tuần.
   - Diễn đạt rõ hành động, mục tiêu và kết quả kỳ vọng để bất kỳ thành viên mới nào tham gia vào nhóm cũng có thể nắm bắt được tiến độ và nhiệm vụ.
3. **Tuyệt đối không tự tiện đưa số liệu chưa chốt hoặc cam kết quá sớm (No Unverified Numbers or Premature Commitments):**
   - **Nghiêm cấm tự bịa hoặc đưa vào tài liệu bất kỳ số liệu cụ thể nào mà nhóm chưa chốt:** Tuyệt đối không tự đưa các con số cứng như chi phí chính xác (*0 VNĐ*), thời gian phản hồi cụ thể (*dưới 1.5s, dưới 200ms*), hoặc các chỉ số hiệu năng chưa qua đo lường thực nghiệm.
   - **Lý do:** Bản Proposal là hồ sơ đề xuất sơ bộ đầu kỳ. Việc đưa vào những con số cam kết tuyệt đối khi chưa có số liệu thực tế sẽ tạo ra rủi ro rất lớn khi nghiệm thu (lỡ khi làm thực tế bị chậm hơn hoặc phát sinh chi phí hạ tầng).
   - **Cách diễn đạt chuẩn:** Diễn đạt dưới dạng định hướng hoặc dự kiến (ví dụ: *"dự toán chi phí dự kiến"*, *"ưu tiên tối ưu ngân sách qua các gói dịch vụ đám mây miễn phí"*, *"tối ưu hóa thời gian phản hồi"* thay vì cam kết *"chi phí 0 VNĐ"* hay *"phản hồi dưới 1.5s"*).

---

### Mục 4: Kế hoạch Nhân sự & Chi phí
- **Cấu trúc nhân sự & Trách nhiệm (RACI):** Phân chia trách nhiệm rõ ràng (Ma trận RACI: Responsible, Accountable, Consulted, Informed hoặc mô hình Scrum).
- **Chi phí nhân sự & Phân bổ công số (Man-Hours Allocation):** 
  - Toàn bộ công số (ví dụ 400 người-giờ) được quản lý tập trung tại đây: Bảng tổng hợp công số 4 Sprint theo thành viên và danh mục chi tiết nhiệm vụ/giờ công của từng thành viên.
  - Giải thích rõ cơ chế quy đổi công số nội bộ của sinh viên (không phát sinh tiền lương thuê ngoài).
- **Kế hoạch chi phí dịch vụ & hạ tầng dự kiến:** 
  - Hạ tầng / Hosting: Ưu tiên gói miễn phí (Free Tier như Vercel, Supabase, Neon) hoặc ước tính chi phí dự kiến.
  - Tên miền, API AI bên thứ ba (Google AI Studio, Resend...).

---

## 2. Tiêu chuẩn Kiểm duyệt Chất lượng

Trước khi bàn giao bản Proposal cho người dùng, AI phải tự kiểm tra:

- [ ] Đã đủ 5 phần chính (Bảng thành viên + 4 mục nội dung) chưa?
- [ ] Dung lượng phát biểu bài toán có vượt quá 2 trang không?
- [ ] Bảng User Story có đúng định dạng chuẩn (As a... I want to... So that...) không?
- [ ] Đã kích hoạt skill `anti-ai-fluff` để lọc sạch từ ngữ sáo rỗng chưa?
- [ ] **Diễn đạt trực quan & Thân thiện non-tech:** Kế hoạch phát triển và thành phẩm đầu ra đã được giải thích rõ ràng về bản chất, nội dung và giá trị chưa? Tuyệt đối không để xảy ra tình trạng ném tên file cộc lốc (`.md`, `.html`, `.docx`...) khiến người đọc không hiểu sản phẩm là gì?
- [ ] **Kiểm tra số liệu & Cam kết chưa chốt:** Đã rà soát và loại bỏ toàn bộ các số liệu cụ thể chưa được nhóm chốt (như khẳng định chi phí 0 VNĐ, thời gian phản hồi dưới X giây...)? Đảm bảo diễn đạt ở mức định hướng/dự kiến an toàn chưa?
- [ ] Đã kiểm tra cách dùng dấu câu, tuyệt đối không lạm dụng dấu chấm phẩy (;) trong văn xuôi và bảng biểu (thay bằng dấu phẩy , hoặc tách câu bằng dấu chấm .)?
- [ ] Đã kiểm tra quy tắc viết hoa, không viết hoa tùy tiện danh từ chung ở giữa câu (như "Nhật ký", "Điểm tương thích", "Bảng phân tích"...)?
- [ ] Đã kiểm tra cách dùng dấu ngoặc đơn, hạn chế tối đa mở ngoặc đơn chú thích và không kẹp kè dịch song ngữ Anh - Việt trong ngoặc đơn?
- [ ] Tất cả liên kết trong tài liệu đều dùng đường dẫn tương đối (relative path) chưa?
