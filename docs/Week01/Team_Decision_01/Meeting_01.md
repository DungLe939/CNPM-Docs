---
title: "Biên bản Họp nhóm Số 01 (Meeting Minutes 01)"
project: "Đồ án Nhập môn Công nghệ Phần mềm"
date: "12/10/2026"
time: "20:25 – 22:00"
location: "Google Meet"
status: "Đã hoàn thành"
---

# BIÊN BẢN HỌP NHÓM SỐ 01

| Thông tin cuộc họp | Chi tiết |
| :--- | :--- |
| **Dự án** | Đồ án Nhập môn Công nghệ Phần mềm |
| **Thời gian** | 20:25 – 22:00, Thứ Hai, ngày 12/10/2026 |
| **Hình thức / Địa điểm** | Trực tuyến qua Google Meet |
| **Chủ trì cuộc họp** | Lê Tấn Dũng |
| **Thư ký ghi chép** | Lê Tấn Dũng |
| **Mục đích chính** | Lên kế hoạch chia repository, chọn phương pháp & phần mềm quản lý, thống nhất kiến trúc công nghệ và kế hoạch chốt đề tài |

---

## 1. Thành phần tham dự

| STT | Họ và tên | Vai trò dự kiến | Trạng thái tham dự |
| :---: | :--- | :--- | :---: |
| 1 | Lê Tấn Dũng | Thành viên nhóm | Có mặt |
| 2 | Võ Nguyễn Việt Hoàng | Thành viên nhóm | Có mặt |
| 3 | Võ Minh Khoa | Thành viên nhóm | Có mặt |
| 4 | Đỗ Chí Cao | Thành viên nhóm | Có mặt |

- **Tổng số thành viên:** 4/4 (Tỷ lệ tham dự: 100%).

---

## 2. Mục tiêu cuộc họp

1. Thống nhất chiến lược tổ chức và phân chia kho lưu trữ mã nguồn (Repository Structure).
2. Lựa chọn phương pháp luận phát triển phần mềm và phần mềm quản lý tiến độ.
3. Thống nhất mô hình ứng dụng và khung công nghệ (Tech Stack) cốt lõi.
4. Lập kế hoạch và thời hạn chốt ý tưởng đề tài đồ án môn học.

---

## 3. Nội dung thảo luận & Quyết định

### 3.1. Phân chia cấu trúc Repository
Nhóm đã xem xét các phương án quản lý mã nguồn và thống nhất mô hình phân tách theo thành phần (Component-based Repositories) có liên kết qua một Repository cha:

- **Các repository con:**
  - `FE (Frontend Repo)`: Quản lý toàn bộ mã nguồn giao diện người dùng, cấu hình build và assets của phía client.
  - `BE (Backend Repo)`: Quản lý mã nguồn API, logic nghiệp vụ, cấu hình kết nối cơ sở dữ liệu và migrations.
  - `Docs (Documentation Repo)`: Quản lý toàn bộ tài liệu môn học, báo cáo tiến độ tuần, biên bản họp, tài liệu phân tích thiết kế và file đặc tả.
- **Repository cha (Parent / Meta Repo):**
  - Bao bọc và liên kết cả 3 repo con (`FE`, `BE`, `Docs`) theo cơ chế Git Submodules hoặc cấu trúc lồng nhau (nested repo).
  - Đóng vai trò làm đầu mối điều phối, quản lý tổng thể tiến độ và tài liệu chung của đồ án.

### 3.2. Phương pháp luận & Phần mềm quản lý dự án
- **Phương pháp quản lý:** Áp dụng mô hình **Scrum** (Agile). Nhóm sẽ vận hành theo các Sprint ngắn hạn tương ứng với từng mốc báo cáo tuần, duy trì họp định kỳ để rà soát backlog và giao việc.
- **Phần mềm quản trị:** Sử dụng **Jira Software** để khởi tạo dự án Scrum, quản lý Product Backlog, lập kế hoạch Sprint, chia nhỏ User Stories thành các Task cụ thể và theo dõi tiến độ từng thành viên.

### 3.3. Phương án thực thi & Khung công nghệ (Tech Stack)
- **Mô hình hệ thống:** Xây dựng ứng dụng web (**Web Application**).
- **Quy trình kỹ thuật ban đầu:** Bắt đầu xác định và tổng hợp các yêu cầu kỹ thuật (Requirements Engineering) ngay sau khi chọn đề tài.
- **Công nghệ cốt lõi:**
  - **Frontend:** `Next.js` (React framework hỗ trợ server-side rendering, routing mạnh mẽ, hiệu năng cao).
  - **Backend:** `NestJS` (Node.js framework theo kiến trúc module, hỗ trợ TypeScript và Dependency Injection rõ ràng).
  - **Cơ sở dữ liệu (Database):** `PostgreSQL` (Hệ quản trị CSDL quan hệ chuẩn mực, đảm bảo tính toàn vẹn và mở rộng dữ liệu).

### 3.4. Kế hoạch chốt ý tưởng đề tài (Project Idea)
- **Tình trạng:** Tại buổi họp ngày 12/10/2026, nhóm đã thảo luận một số định hướng nhưng **chưa chốt đề tài chính thức**.
- **Kế hoạch:** Mỗi thành viên chủ động nghiên cứu và chuẩn bị tối thiểu 1 đề xuất ý tưởng bài toán thực tế phù hợp với mô hình Web App và yêu cầu môn học.
- **Hạn chót thống nhất (Deadline):** Chậm nhất trước **20:00 - Thứ Tư, ngày 14/10/2026**.

---

## 4. Kế hoạch hành động tiếp theo (Action Items)

| STT | Đầu việc | Người phụ trách | Hạn chót (Deadline) | Trạng thái |
| :---: | :--- | :--- | :---: | :---: |
| 1 | Chuẩn bị 1 - 2 ý tưởng đề tài phần mềm cụ thể | Cả 4 thành viên | 20:00, 14/10/2026 | Đang tiến hành |
| 2 | Họp nhóm biểu quyết chọn đề tài chính thức & phân chia vai trò (Leader, FE, BE, QA) | Cả 4 thành viên | Tối 14/10/2026 | Chờ thực hiện |
| 3 | Khởi tạo dự án Scrum trên Jira Software và mời các thành viên tham gia | Lê Tấn Dũng | 15/10/2026 | Chờ thực hiện |
| 4 | Thiết lập cấu trúc các repository trên GitHub (Parent repo, FE, BE, Docs) | Cả nhóm | 16/10/2026 | Chờ thực hiện |

---

## 5. Xác nhận cuộc họp

- **Thời gian kết thúc:** 22:00 cùng ngày (12/10/2026).
- **Kết quả biểu quyết:** 4/4 thành viên (100%) tham dự đã thống nhất toàn bộ các nội dung và quyết định trong biên bản này.
- **Ghi chú cập nhật:** Nhóm sẽ cập nhật bổ sung vai trò chi tiết và đề tài chính thức sau buổi họp chốt ý tưởng vào ngày 14/10/2026.
