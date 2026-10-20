# Kế hoạch triển khai HireUS Tools

> Cập nhật ngày 20/10/2026 theo [Proposal đã được người dùng kiểm tra](../../Submission/Project_Proposal.md) và [bản HTML](../../Submission/Project_Proposal.html).
> Tài liệu này tổng hợp kế hoạch từ Proposal, không phải biên bản phê duyệt hay báo cáo tính năng đã hoàn thành.

## 1. Phạm vi

HireUS Tools phục vụ sinh viên IT tìm việc Intern/Fresher, gồm 4 phân hệ:

| Phân hệ | Nội dung |
| :--- | :--- |
| 1. CV Builder & SeekerBot | Tạo, chỉnh sửa CV, gợi ý nội dung theo STAR và xuất PDF. |
| 2. Voice Mock Interview | Luyện phỏng vấn kỹ thuật bằng giọng nói Việt/Anh, hỏi đáp theo ngữ cảnh và nhận báo cáo đánh giá. |
| 3. Job Matching & Skill Gap | Đối chiếu CV với JD, tính điểm tương thích và gợi ý kỹ năng cần bổ sung. |
| 4. Job Tracking | Theo dõi tin từ Fanpage/LinkedIn, lọc tin bằng AI và thông báo đợt tuyển Intern/Fresher. |

## 2. Công nghệ dự kiến

| Thành phần | Công nghệ theo Proposal |
| :--- | :--- |
| Frontend | Next.js, Web Audio API |
| Backend | NestJS, TypeScript, Task Scheduling |
| Cơ sở dữ liệu | PostgreSQL, Prisma ORM |
| Dịch vụ AI | FastAPI trên Kaggle, DeepSeek API, mô hình âm thanh Hugging Face |
| Đóng gói | Docker Compose chạy cục bộ |
| Quản lý | Scrum trên Jira, mã nguồn trên GitHub |

Chi tiết cấu hình và dự toán dịch vụ xem mục 3.3 và 5.3 của Proposal. Đây là thông tin kế hoạch, chưa phải kết quả vận hành thực tế.

## 3. Kế hoạch 8 tuần

Dự án triển khai trong 8 tuần theo mô hình **Scrum** trên **Jira**, chia thành 4 chu kỳ Sprint (2 tuần/Sprint):

| Chu kỳ Sprint | Tuần | Công việc trọng tâm | Thành phẩm cụ thể đầu ra |
| :---: | :---: | :--- | :--- |
| **Sprint 1** | **Tuần 01** | Khảo sát nhu cầu, thống nhất ý tưởng, lập Jira Backlog và hoàn thiện hồ sơ đề xuất đồ án. | - Hồ sơ Project Proposal hoàn chỉnh.<br>- Biên bản làm việc nhóm & phân công. |
| | **Tuần 02** | Tiếp nhận góp ý từ GV, tinh chỉnh Backlog, dựng khung mã nguồn mẫu Next.js & NestJS. | - Bảng Scrum Backlog trên Jira.<br>- Khung mã nguồn dự án trên GitHub. |
| **Sprint 2** | **Tuần 03** | Lập Use Case chi tiết, vẽ Activity & Sequence Diagram cho 4 phân hệ. | - Hồ sơ đặc tả yêu cầu phần mềm. |
| | **Tuần 04** | Thiết kế Wireframe 4 màn hình, thiết kế lược đồ cơ sở dữ liệu PostgreSQL (ERD) và danh mục REST API. | - Hồ sơ thiết kế kiến trúc phần mềm.<br>- Bản vẽ Wireframe & kịch bản tạo CSDL. |
| **Sprint 3** | **Tuần 05** | Cài đặt Auth JWT, lập trình Phân hệ 1 (Tạo CV ATS & Trợ lý SeekerBot AI trên Kaggle). | - Module đăng ký/đăng nhập hoàn tất.<br>- Chức năng tạo CV ATS chạy thực nghiệm. |
| | **Tuần 06** | Lập trình Phân hệ 2 (Phỏng vấn giọng nói AI hai chiều) và Phân hệ 3 (Đối soát Job & Skill Gap). | - Bản chạy thực nghiệm phỏng vấn giọng nói.<br>- Bản chạy thực nghiệm so khớp hồ sơ và JD. |
| **Sprint 4** | **Tuần 07** | Lập trình Phân hệ 4 (Săn tin tuyển dụng mạng xã hội), tối ưu API và viết Jest Unit Tests. | - Bản chạy hệ thống quét tin tuyển dụng.<br>- Bộ kiểm thử tự động Jest (Coverage $\ge 70\%$). |
| | **Tuần 08** | Đóng gói Docker Compose chạy cục bộ, kiểm thử tích hợp, quay video demo và slide báo cáo. | - Sản phẩm Web hoàn chỉnh chạy qua Docker.<br>- Video demo, slide báo cáo & tài liệu cài đặt. |

## 4. Phân công

Do dự án gồm 4 thành viên, mỗi thành viên đều có thế mạnh khác nhau nên các nhiệm vụ được phân công theo thế mạnh chuyên môn của từng thành viên.

| STT | Thành viên | Vai trò dự án | Nhiệm vụ kỹ thuật trọng tâm | Phân hệ phụ trách |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Lê Tấn Dũng** | Trưởng nhóm / PM & Kỹ sư AI | Quản trị dự án trên Jira, viết code dịch vụ FastAPI trên Kaggle và mở cổng API kết nối hệ thống | Phân hệ 2 (AI phỏng vấn) & Phân hệ 4 (Săn tin tuyển dụng) |
| **2** | **Võ Nguyễn Việt Hoàng** | Kỹ sư AI & Dữ liệu | Tích hợp DeepSeek API, thuật toán so khớp Job Match và mô hình phân loại tin | Phân hệ 2 (AI phỏng vấn), Phân hệ 3 (Đối soát Job) & Phân hệ 4 |
| **3** | **Võ Minh Khoa** | Lập trình viên Fullstack | Phát triển giao diện Next.js, xây dựng hệ thống API máy chủ NestJS | Phân hệ 1 (Tạo CV chuẩn ATS) & Phân hệ 3 (Đối soát Job) |
| **4** | **Đỗ Chí Cao** | Kỹ sư CSDL & Kiểm thử (QA) | Thiết kế cơ sở dữ liệu PostgreSQL và kiểm thử chất lượng hệ thống | Quản trị cơ sở dữ liệu & Kiểm thử toàn diện |

## 5. Công số dự kiến

Nhằm đảm bảo đúng tiến độ, nhóm đề xuất định mức **8 giờ / người / tuần**. Tổng công số toàn nhóm trong 8 tuần là **256 người-giờ** (64 giờ / thành viên):
| Chu kỳ Sprint | Nội dung trọng tâm | Lê Tấn Dũng | Võ Nguyễn Việt Hoàng | Võ Minh Khoa | Đỗ Chí Cao | Tổng Sprint |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **Sprint 1** *(Tuần 1 - 2)* | Khởi động, chọn đề tài & hoàn thiện proposal | 16h | 16h | 16h | 16h | **64h** |
| **Sprint 2** *(Tuần 3 - 4)* | Đặc tả yêu cầu chi tiết & thiết kế kiến trúc/CSDL | 16h | 16h | 16h | 16h | **64h** |
| **Sprint 3** *(Tuần 5 - 6)* | Cài đặt CV ATS, trợ lý SeekerBot & AI phỏng vấn | 16h | 16h | 16h | 16h | **64h** |
| **Sprint 4** *(Tuần 7 - 8)* | Cài đặt săn tin mạng xã hội, kiểm thử & đóng gói Docker | 16h | 16h | 16h | 16h | **64h** |
| **TỔNG CỘNG** | **Toàn bộ 8 tuần (4 Sprint)** | **64h** | **64h** | **64h** | **64h** | **256h** |

## 6. Giới hạn của bản kế hoạch

- Chức năng tự động gửi hồ sơ qua email trong bản cũ không nằm trong phạm vi Proposal hiện tại.
- Các chỉ tiêu độ trễ dưới 1,5 giây, độ chính xác phân loại 90% và trích xuất PDF 100% trong bản cũ không được dùng làm cam kết vì chưa có trong nguồn chuẩn.
- Lược đồ dữ liệu, giao thức truyền âm thanh, mô hình AI cụ thể và bộ tiêu chí chấm phỏng vấn cần được xác định ở giai đoạn phân tích, thiết kế. Các mô tả cũ không được coi là quyết định đã chốt.
- Mục tiêu Jest coverage từ 70% là kế hoạch trong Proposal, chưa phải kết quả kiểm thử.
