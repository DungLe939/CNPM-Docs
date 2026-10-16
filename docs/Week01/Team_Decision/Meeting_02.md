---
title: "Biên bản Họp nhóm Số 02 (Meeting Minutes 02)"
project: "Đồ án Nhập môn Công nghệ Phần mềm"
date: "14/10/2026"
time: "20:00 – 21:30"
location: "Google Meet"
status: "Đã hoàn thành"
---

# BIÊN BẢN HỌP NHÓM SỐ 02

| Thông tin cuộc họp | Chi tiết |
| :--- | :--- |
| **Dự án** | Đồ án Nhập môn Công nghệ Phần mềm |
| **Thời gian** | 20:00 – 21:30, Thứ Tư, ngày 14/10/2026 |
| **Hình thức / Địa điểm** | Trực tuyến qua Google Meet |
| **Chủ trì cuộc họp** | Lê Tấn Dũng |
| **Thư ký ghi chép** | Lê Tấn Dũng |
| **Mục đích chính** | Báo cáo ý tưởng đề tài, biểu quyết chọn đề tài chính thức và phân công vai trò trách nhiệm các thành viên |

---

## 1. Thành phần tham dự

| STT | Họ và tên | Vai trò phân công chính thức | Trạng thái tham dự |
| :---: | :--- | :--- | :---: |
| 1 | Lê Tấn Dũng | Trưởng nhóm (Leader) / AI Lead | Có mặt |
| 2 | Võ Nguyễn Việt Hoàng | Frontend Developer / UI Lead | Có mặt |
| 3 | Võ Minh Khoa | Backend Developer | Có mặt |
| 4 | Đỗ Chí Cao | Database Administrator & QA/QC Lead | Có mặt |

- **Tổng số thành viên:** 4/4 (Tỷ lệ tham dự: 100%).

---

## 2. Mục tiêu cuộc họp

1. Lắng nghe đề xuất ý tưởng đề tài từ các thành viên (theo hạn chót 20:00 ngày 14/10 đã giao tại [Meeting_01.md](./Meeting_01.md)).
2. Phân tích ưu/nhược điểm, tính khả thi và biểu quyết chọn 01 đề tài chính thức cho đồ án môn học.
3. Thống nhất phân chia vai trò và trách nhiệm cụ thể của từng thành viên trong nhóm.
4. Xác định phạm vi 5 phân hệ kỹ thuật ban đầu để phục vụ việc lập Kế hoạch triển khai chi tiết.

---

## 3. Nội dung thảo luận & Quyết định

### 3.1. Đánh giá các đề xuất đề tài & Biểu quyết
Các thành viên đã trình bày các hướng tiếp cận bài toán:
- *Ý tưởng 1:* Sàn đấu giá nông sản trực tuyến (khó kiểm chứng thực tế và thiếu tính ứng dụng cho sinh viên).
- *Ý tưởng 2:* Hệ thống quản lý và chăm sóc sức khỏe cá nhân (phạm vi rộng, rủi ro về độ chính xác dữ liệu y tế).
- *Ý tưởng 3:* **Nền tảng Tối ưu CV, Mô phỏng Phỏng vấn Kỹ thuật AI & Săn việc làm IT cho Intern/Fresher (JobSeeker AI).**

👉 **Kết quả biểu quyết:** 4/4 thành viên (100% đồng thuận) quyết định chọn đề tài: **JobSeeker AI**.  
*Lý do:* Giải quyết trực tiếp nhu cầu cấp thiết của sinh viên IT khi tìm việc thực tập; kết hợp hài hòa giữa phát triển Web Application chuẩn mực (`Next.js` + `NestJS` + `PostgreSQL`) và ứng dụng công nghệ GenAI (`Gemini API`) đúng định hướng môn học.

### 3.2. Phân công vai trò & Trách nhiệm nhóm (RACI)
- **Lê Tấn Dũng (Leader / AI Lead):**
  - Quản trị dự án tổng thể, điều phối Sprint trên Jira Scrum.
  - Phụ trách tích hợp Google Gemini API, xây dựng Social Post AI Classifier Service.
  - Chủ trì soạn thảo tài liệu kỹ thuật môn học (Proposal, SRS, SDD, Final Report).
- **Võ Nguyễn Việt Hoàng (Frontend Dev / UI Lead):**
  - Thiết kế giao diện Figma cho 5 phân hệ người dùng.
  - Lập trình Web Client trên Next.js 14, module CV Builder (PDF text layer) và giao diện Audio Interview.
- **Võ Minh Khoa (Backend Dev):**
  - Xây dựng hệ thống REST API, Authentication JWT trên NestJS.
  - Phát triển module Auto Email Dispatcher gửi CV qua SMTP (Nodemailer) kèm Rate Limiting.
- **Đỗ Chí Cao (Database & QA/QC Lead):**
  - Thiết kế và quản trị cơ sở dữ liệu quan hệ PostgreSQL (Schema migrations, Indexing).
  - Thiết kế Test Cases, thực hiện kiểm thử tự động (Jest) và kiểm thử chất lượng hệ thống (QA/QC).

### 3.3. Thống nhất 5 Phân hệ Kỹ thuật Cốt lõi
Nhóm đã thống nhất phạm vi chức năng của hệ thống gồm 5 phân hệ:
1. **CV Builder & SeekerBot:** Tạo CV chuẩn ATS layout 1 cột, xuất PDF text layer 100%, chatbot gợi ý viết đạn mô tả dự án theo chuẩn Google XYZ / STAR.
2. **Real-time Voice AI Technical Mock Interview:** Phỏng vấn kỹ thuật 1:1 bằng giọng nói với AI Tech Lead, chấm 3 tiêu chí: *Kiến thức nền tảng, Tư duy giải quyết vấn đề, Diễn đạt kỹ thuật*.
3. **Automated & Assisted Job Application Dispatcher:** Soạn Cover Letter cá nhân hóa bám sát JD và nộp hồ sơ an toàn qua email HR trực tiếp (SMTP).
4. **Job Aggregator & Market Skills Gap Analysis Dashboard:** Thu thập tin việc làm, đối sánh kỹ năng và phân tích lộ trình bù đắp lỗ hổng kỹ năng cho sinh viên.
5. **Early Career Radar (Social Job Alert):** Quét bài đăng Fanpage/LinkedIn của các công ty công nghệ (VNG, Bosch, NAB, Maven...), dùng LLM phân loại giữ lại tin Intern/Fresher và trích xuất hạn nộp.

> 📎 **Tài liệu Kế hoạch Triển khai Chi tiết (Implementation Plan Reference):**  
> - **Bản Markdown nội bộ:** [JobSeeker_Implementation_Plan.md](./Material/JobSeeker_Implementation_Plan.md) ⏐ **Bản gốc Google Drive:** [Xem trên Google Drive](https://drive.google.com/file/d/1s8uYv3yBGpx7TyCsTtIVSbNTrC8LbDbY/view)  
> - **Bản HTML Visualization:** [JobSeeker_Implementation_Plan.html](./Material/JobSeeker_Implementation_Plan.html) ⏐ **Bản gốc Google Drive:** [Xem trên Google Drive](https://drive.google.com/file/d/1eLih_N3dm8BvZAxLCbiSyRzQsOIz-I3H/view)  
> - **Thư mục lưu trữ Google Drive của nhóm:** [CNPM Team Drive Folder](https://drive.google.com/drive/folders/12e0__KnGQOQayRmNEWwYPrq-0ErlqGph)

---

## 4. Kế hoạch hành động tiếp theo (Action Items)

| STT | Đầu việc cụ thể | Người phụ trách | Hạn chót (Deadline) | Trạng thái |
| :---: | :--- | :--- | :---: | :---: |
| 1 | Soạn thảo Kế hoạch Triển khai Chi tiết ([JobSeeker_Implementation_Plan.md](./Material/JobSeeker_Implementation_Plan.md) ⏐ [Bản Drive](https://drive.google.com/file/d/1s8uYv3yBGpx7TyCsTtIVSbNTrC8LbDbY/view)) | Lê Tấn Dũng | 15/10/2026 | Hoàn thành |
| 2 | Khởi tạo bảng Jira Scrum Board và nhập Backlog ban đầu | Lê Tấn Dũng | 15/10/2026 | Hoàn thành |
| 3 | Khởi tạo cấu trúc các repository (`FE`, `BE`, `Docs`) trên GitHub | Cả 4 thành viên | 16/10/2026 | Đang thực hiện |
| 4 | Soạn thảo bản Đề xuất đồ án đợt 1 ([Project_Proposal.md](../../Week02/)) chuẩn 5 phần | Lê Tấn Dũng & Nhóm | 19/10/2026 | Chờ thực hiện |

---

## 5. Xác nhận cuộc họp

- **Thời gian kết thúc:** 21:30 cùng ngày (14/10/2026).
- **Kết quả xác nhận:** Toàn bộ 4 thành viên nhóm đã thống nhất và cam kết thực hiện đúng trách nhiệm được phân công trong biên bản này.
