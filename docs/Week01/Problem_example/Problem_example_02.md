---
title: "Ví dụ Phát biểu Bài toán: Ứng dụng theo dõi sức khỏe"
document_type: "Tài liệu mẫu tham khảo (Reference Spec)"
template_section: "Mục 2 - Phát biểu bài toán sơ lược (Project Proposal)"
instructor: "Thầy Nguyễn Ngô Duy Khoa (nndkhoa)"
source_spec: "https://hackmd.io/@nndkhoa9/se-healthmonitor-spec"
related_spec: "https://hackmd.io/@nndkhoa9/se-onlineauction-spec"
date_created: "12/10/2026"
---

# TÀI LIỆU MẪU: PHÁT BIỂU BÀI TOÁN SƠ LƯỢC

> **Nguồn trích dẫn:** Trích từ **Mục 2 - Phát biểu bài toán sơ lược** trong file mẫu `Template#0-ProjectProposal-2022.docx` (Khoa CNTT - ĐH KHTN TP.HCM).  
> **Link tham khảo gốc của Giảng viên:**  
> - [HackMD: se-healthmonitor-spec](https://hackmd.io/@nndkhoa9/se-healthmonitor-spec)  
> - [HackMD: se-onlineauction-spec](https://hackmd.io/@nndkhoa9/se-onlineauction-spec)

---

## 📌 Hướng dẫn & Lưu ý từ Giảng viên (Template Guidance)

- **Phạm vi nội dung:**
  - Nhóm sinh viên mô tả bài toán của dự án trong khoảng **1 - 2 trang** nghiệp vụ.
  - Cần nêu rõ **môi trường hoạt động** (Ví dụ: Web browser hỗ trợ HTML5, server: Node.js/Apache/Nginx, hệ điều hành,...).
  - Cần xác định các **ràng buộc về thiết kế & triển khai** (Ví dụ: ngôn ngữ lập trình, hệ quản trị cơ sở dữ liệu, chuẩn tài liệu, bảo mật,...).
- **Lưu ý cốt lõi:**
  - Ở đợt nộp **Proposal**, sinh viên **chỉ phát biểu bài toán ở mức độ sơ lược**.
  - Tránh viết quá dài hoặc đi sâu vào từng ca sử dụng (Use Case Details). Phát biểu bài toán chi tiết sẽ được trình bày trong tài liệu phân tích ở các tuần tiếp theo.

---

# ĐẶC TẢ BÀI TOÁN MẪU: ỨNG DỤNG THEO DÕI SỨC KHỎE

> **Vai trò:** Trưởng nhóm phát triển ứng dụng di động & thiết bị đeo thông minh  
> **Lĩnh vực:** Y tế số & Thể dục thể thao (Digital Health & Fitness Tracking)  
> **Kiến trúc:** 2 phân hệ tích hợp: **Smartwatch App** & **Smartphone App**

---

## 1. Tổng quan hệ thống

Hệ thống theo dõi sức khỏe kết nối giữa thiết bị đeo (**Smartwatch**) và điện thoại di động (**Smartphone**) nhằm hỗ trợ người dùng theo dõi hoạt động thể chất, phân tích dữ liệu vận động và quản lý thói quen rèn luyện thể thao.

Hệ thống được chia thành 2 phân hệ độc lập nhưng đồng bộ chặt chẽ:
- **Phân hệ Smartwatch:** Ghi nhận và hiển thị các chỉ số sinh trắc học và vận động tức thời trong quá trình người dùng luyện tập.
- **Phân hệ Smartphone:** Lưu trữ lịch sử, phân tích số liệu thống kê chuyên sâu, lập lịch biểu rèn luyện, nhắc nhở thông minh và chia sẻ mạng xã hội.

---

## 2. Phân hệ Đồng hồ thông minh (Smartwatch Subsystem)

### 2.1. Nhận diện & Kích hoạt phiên luyện tập
- **Cơ chế tự động:** Khi người dùng đeo đồng hồ và bắt đầu vận động, hệ thống tự động nhận diện loại hoạt động đang diễn ra.
- **Các môn thể thao hỗ trợ:** Đi bộ, chạy bộ, đạp xe, bơi lội,...
- **Kích hoạt:** Tự động bật chức năng thu thập và theo dõi chỉ số sức khỏe.

### 2.2. Ghi nhận & Hiển thị thông số thời gian thực
Thông qua GPS tích hợp và các cảm biến chuyển động (accelerometer/gyroscope), cảm biến quang học đo nhịp tim (PPG):
- Quãng đường di chuyển hiện tại.
- Thời gian vận động trôi qua.
- Tốc độ trung bình (Average Pace / Speed).
- Nhịp tim tức thời (Current Heart Rate - bpm).

### 2.3. Kết thúc & Lưu trữ tạm thời
- Khi hoàn thành buổi tập, người dùng chủ động ra lệnh kết thúc trên màn hình đồng hồ.
- Phân hệ smartwatch lập tức dừng theo dõi và lưu trữ tạm thời dữ liệu buổi tập vào bộ nhớ cục bộ (Local Cache).

---

## 3. Cơ chế kết nối & Đồng bộ dữ liệu (Connectivity & Data Sync)

### 3.1. Đồng bộ qua Bluetooth
- Khi hai thiết bị được ghép đôi (pairing) qua sóng Bluetooth, dữ liệu lưu tạm trên smartwatch sẽ tự động đồng bộ và tải lên phân hệ smartphone.

### 3.2. Chia sẻ mạng xã hội (Social Sharing)
- Phân hệ smartphone cho phép người dùng chia sẻ trực tiếp kết quả, lộ trình và thành tích của buổi tập lên các nền tảng mạng xã hội: Facebook, Twitter/X, Instagram,...

---

## 4. Phân hệ Điện thoại di động (Smartphone Subsystem)

### 4.1. Quản lý lịch sử & Báo cáo tổng hợp
- **Danh sách hoạt động:** Hiển thị toàn bộ các buổi tập theo trình tự thời gian đảo ngược (mới nhất lên đầu).
- **Thống kê vĩ mô:** Tổng số phiên hoạt động, tổng quãng đường di chuyển được tổng hợp và phân loại theo **Tuần**, **Tháng** và **Năm**.

### 4.2. Phân tích chi tiết từng buổi tập (Detailed Activity Analysis)
Khi người dùng chọn một buổi tập cụ thể trong danh sách, hệ thống hiển thị:
1. **Lộ trình trực quan:** Vẽ đường đi GPS trên nền bản đồ số được tích hợp từ dịch vụ bản đồ trung gian (Map Service API như Google Maps / Mapbox / Apple Maps).
2. **Chỉ số tổng quát:**
   - Tổng thời gian thực hiện.
   - Tổng quãng đường di chuyển.
   - Lượng calo tiêu thụ (kcal).
   - Độ cao thay đổi trong suốt hành trình (Elevation Gain / Loss).
3. **Chỉ số chuyên sâu & Biểu đồ phân tích:**
   - Tốc độ / nhịp tim trung bình trên toàn lộ trình.
   - Tốc độ / nhịp tim chi tiết theo từng km (Split time / Split heart rate).
   - Biểu đồ trực quan biểu diễn sự biến thiên của tốc độ và nhịp tim theo dòng thời gian.

---

## 5. Lập lịch biểu & Theo dõi mục tiêu (Scheduling & Goal Management)

### 5.1. Thiết lập lịch biểu rèn luyện
Hỗ trợ người dùng tạo các lịch biểu vận động có tính chất lặp lại định kỳ:
- Tên hoạt động thể chất.
- Loại hình hoạt động: Đi bộ, chạy bộ, đạp xe, bơi lội, hoặc môn thể thao khác.
- Tần suất lặp lại: Hàng ngày hoặc các ngày cụ thể trong tuần.
- Cấu hình thông báo nhắc nhở: Bật/Tắt nhắc nhở, khoảng thời gian báo trước (ví dụ: trước 15, 30 phút).

### 5.2. Đặt mục tiêu & Đánh giá kết quả
- **Tiêu chí mục tiêu:** Người dùng có thể đặt chỉ tiêu cụ thể cho từng buổi tập theo:
  - Quãng đường cần đạt (km).
  - Thời gian hoàn thành (phút).
  - Tốc độ trung bình (km/h hoặc pace).
- **Hệ thống phản hồi thông minh:**
  - Nếu **không đạt mục tiêu**: Ứng dụng đưa ra lời khuyên động viên tích cực, khích lệ người dùng cố gắng hơn ở phiên tiếp theo.
  - Đề xuất người dùng chủ động điều chỉnh lại mục tiêu cho phù hợp với thể trạng thực tế.

---

## 6. Ma trận phân chia chức năng theo phân hệ

| STT | Nhóm chức năng | Phân hệ Smartwatch | Phân hệ Smartphone |
| :---: | :--- | :---: | :---: |
| 1 | Tự động nhận diện hoạt động thể chất | ✅ | ❌ |
| 2 | Đo nhịp tim, tốc độ, quãng đường tức thời | ✅ | ❌ |
| 3 | Lưu trữ tạm dữ liệu khi ngoại tuyến | ✅ | ❌ |
| 4 | Đồng bộ dữ liệu qua Bluetooth | ✅ | ✅ |
| 5 | Tích hợp dịch vụ bản đồ (Map Service API) | ❌ | ✅ |
| 6 | Thống kê vĩ mô (Tuần / Tháng / Năm) | ❌ | ✅ |
| 7 | Vẽ biểu đồ biến thiên tốc độ, nhịp tim | ❌ | ✅ |
| 8 | Lập lịch biểu và gửi thông báo nhắc nhở | ❌ | ✅ |
| 9 | Quản lý mục tiêu & Phản hồi động viên | ❌ | ✅ |
| 10 | Chia sẻ thành tích lên Mạng xã hội | ❌ | ✅ |

---

## 7. Ràng buộc thiết kế & Môi trường hoạt động

- **Phần cứng & Thiết bị đeo:** Đồng hồ thông minh tích hợp chip GPS, cảm biến gia tốc, con quay hồi chuyển, cảm biến đo nhịp tim quang học (PPG), hỗ trợ Bluetooth Low Energy (BLE).
- **Hệ điều hành:**
  - Smartwatch OS: Wear OS / watchOS / RTOS chuyên dụng.
  - Smartphone OS: Android / iOS.
- **Tích hợp bên thứ ba:**
  - Map Service API (Google Maps Platform, Mapbox API, v.v.).
  - Social Network SDKs (Facebook Graph API, X API, Instagram Graph API).
