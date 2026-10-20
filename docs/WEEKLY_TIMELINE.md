# Tiến độ và kế hoạch dự án

> Cập nhật ngày 20/10/2026. Nguồn kế hoạch: [Proposal đã được người dùng kiểm tra](./Week01/Submission/Project_Proposal.md).

## Trạng thái có căn cứ

- Đã có [Proposal Markdown](./Week01/Submission/Project_Proposal.md) và [HTML](./Week01/Submission/Project_Proposal.html), được người dùng xác nhận đã kiểm tra. Chưa có xác nhận đã nộp bài hoặc được giảng viên duyệt.
- Có hai bản ghi họp ngày 12/10 và 14/10 trong [biên bản 01](./Week01/Team_Decision/Meeting_01.md) và [biên bản 02](./Week01/Team_Decision/Meeting_02.md). Nội dung lịch sử chưa được xác minh lại từ nguồn gốc.
- Đã đồng bộ tài liệu tổng quan và [kế hoạch triển khai](./Week01/Team_Decision/Material/HireUS_Implementation_Plan.md) theo phạm vi 4 phân hệ của Proposal.
- Chưa xác nhận trạng thái Jira, các repo FE/BE, tiến độ lập trình hoặc kiểm thử. Không đánh dấu các việc này đã hoàn thành chỉ dựa trên kế hoạch.

## Kế hoạch theo Proposal

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

## Tài liệu hiện có

- Hồ sơ Proposal nằm tại `Week01/Submission/`, không phải `Week02/`.
- [Thông báo môn học](./Week01/Material/Thông_báo_1.md) và [template PDF](./Week01/Material/Template%230-ProjectProposal-2022.pdf).
- Hai bài toán tham khảo: [sàn đấu giá](./Week01/Problem_example/Problem_example_01_raw.md) và [theo dõi sức khỏe](./Week01/Problem_example/Problem_example_02_raw.md).

Ngày nộp cụ thể và trạng thái từng tuần cần cập nhật từ thông báo hoặc kết quả thực tế của nhóm.
