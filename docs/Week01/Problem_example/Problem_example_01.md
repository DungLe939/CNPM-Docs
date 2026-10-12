---
title: "Ví dụ Phát biểu Bài toán: Sàn đấu giá trực tuyến"
document_type: "Tài liệu mẫu tham khảo (Reference Spec)"
template_section: "Mục 2 - Phát biểu bài toán sơ lược (Project Proposal)"
instructor: "Thầy Nguyễn Ngô Duy Khoa (nndkhoa)"
source_spec: "https://hackmd.io/@nndkhoa9/se-onlineauction-spec"
related_spec: "https://hackmd.io/@nndkhoa9/se-healthmonitor-spec"
date_created: "12/10/2026"
---

# TÀI LIỆU MẪU: PHÁT BIỂU BÀI TOÁN SƠ LƯỢC

> **Nguồn trích dẫn:** Trích từ **Mục 2 - Phát biểu bài toán sơ lược** trong file mẫu `Template#0-ProjectProposal-2022.docx` (Khoa CNTT - ĐH KHTN TP.HCM).  
> **Link tham khảo gốc của Giảng viên:**  
> - [HackMD: se-onlineauction-spec](https://hackmd.io/@nndkhoa9/se-onlineauction-spec)  
> - [HackMD: se-healthmonitor-spec](https://hackmd.io/@nndkhoa9/se-healthmonitor-spec)

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

# ĐẶC TẢ BÀI TOÁN MẪU: SÀN ĐẤU GIÁ TRỰC TUYẾN

> **Vai trò:** Trưởng nhóm phát triển phần mềm  
> **Lĩnh vực:** Thương mại điện tử - Đấu giá trực tuyến (Online Auction Platform)  
> **Hình thức:** 100% trực tuyến từ khâu đăng sản phẩm, đấu giá đến thanh toán

---

## 1. Tổng quan hệ thống

Sàn đấu giá trực tuyến là hệ thống kết nối **Người bán (Seller)** và **Người mua (Buyer)** thông qua cơ chế đấu giá công khai qua Internet:
- **Người bán:** Đăng tải thông tin sản phẩm và quy định các mức giá, thời hạn.
- **Người mua:** Tìm kiếm sản phẩm quan tâm và tham gia trả giá.
- **Quy tắc trúng đấu giá:** Sản phẩm sẽ thuộc về người mua nào ra **giá hợp lệ cao nhất** khi phiên đấu giá kết thúc (đáp ứng điều kiện giá tối thiểu).

---

## 2. Nghiệp vụ Người bán (Seller) & Quy định đăng bán

### 2.1. Thông tin sản phẩm
Khi đăng sản phẩm, người bán cần cung cấp thông tin trung thực, rõ ràng và chi tiết:
- Tên gọi sản phẩm
- Chủng loại (Category)
- Kích cỡ, trọng lượng
- Tình trạng hiện tại (Mới, đã qua sử dụng, độ hao mòn,...)

### 2.2. Thời hạn đấu giá & Gia hạn
- **Thời hạn mặc định:** 7 ngày (tính từ thời điểm đăng thành công).
- **Gia hạn thời gian:** Cho phép người bán kéo dài thêm thời hạn.
- **Phụ phí gia hạn:** `5.000 VNĐ / ngày`.

### 2.3. Mức giá khởi điểm & Mức giá bán tối thiểu (Reserve Price)
- **Giá khởi điểm (Starting Price):** Mức giá sàn để người mua bắt đầu trả giá.
- **Giá bán tối thiểu (Reserve Price):** Mức giá ngầm để tránh bán dưới kỳ vọng:
  - Nếu kết thúc đấu giá mà giá cao nhất **< Giá bán tối thiểu** $\rightarrow$ **Hủy giao dịch** (không bên nào phải chịu phí).
  - Phụ phí thiết lập giá tối thiểu: `10.000 VNĐ / sản phẩm`.

### 2.4. Phương thức giao nhận hàng
Người bán có 3 lựa chọn hình thức vận chuyển:
1. **Miễn phí giao hàng (Free Shipping):** Người bán chịu phí vận chuyển.
2. **Người mua đến lấy (Local Pickup):** Tự thỏa thuận địa điểm nhận hàng.
3. **Giao hàng qua công ty chuyển phát:** Hệ thống kết nối API với đơn vị vận chuyển để tính phí tự động dựa trên trọng lượng/kích thước và hiển thị minh bạch cho người mua khi xem sản phẩm.

---

## 3. Nghiệp vụ Người mua (Buyer) & Quy tắc trả giá

### 3.1. Tìm kiếm và lọc sản phẩm
Hệ thống cung cấp bộ lọc đa tiêu chí:
- Tên sản phẩm (Từ khóa tìm kiếm)
- Chủng loại danh mục
- Giá hiện tại (Current Bid)
- Hình thức giao nhận

### 3.2. Quy tắc trả giá (Bidding Rules)
- **Điều kiện ra giá:** 
  - Giá đặt mới phải **lớn hơn giá hiện tại**.
  - Bước giá: Giá đặt phải là **bội số của 5.000 VNĐ**.
- **Số lần tham gia:** Không giới hạn số lần người mua trả giá trong thời gian phiên đấu giá còn hiệu lực.

---

## 4. Kết thúc đấu giá & Thanh toán

Khi hết thời hạn đấu giá, hệ thống tự động xử lý theo 2 kịch bản:

| Trường hợp | Điều kiện | Kết quả giao dịch | Nghĩa vụ tài chính |
| :--- | :--- | :--- | :--- |
| **Kịch bản A: Thất bại** | Giá kết thúc < Giá bán tối thiểu | Giao dịch bị **hủy bỏ** | Cả hai bên không mất phí |
| **Kịch bản B: Thành công** | Giá kết thúc $\ge$ Giá bán tối thiểu | Giao dịch **thành công** | - Người bán trả phí đăng tin<br>- Người mua nhận hóa đơn thanh toán |

---

## 5. Bảng biểu phí & Công thức tính toán

### 5.1. Bảng biểu phí hệ thống

| Loại phí | Đơn giá | Điều kiện áp dụng |
| :--- | :--- | :--- |
| **Chi phí đăng gốc** | `10.000 VNĐ` | Bắt buộc cho mỗi sản phẩm (thu khi giao dịch thành công) |
| **Phí gia hạn thời gian** | `5.000 VNĐ / ngày` | Khi người bán kéo dài quá thời hạn 7 ngày mặc định |
| **Phí đặt giá tối thiểu** | `10.000 VNĐ` | Khi người bán kích hoạt tính năng Reserve Price |

### 5.2. Công thức tài chính

- **Chi phí người bán phải trả:**
  $$\text{Chi phí đăng sản phẩm} = \text{Chi phí gốc (10.000)} + \text{Phí gia hạn (nếu có)} + \text{Phí giá tối thiểu (nếu có)}$$

- **Số tiền người mua phải thanh toán:**
  $$\text{Tiền mua sản phẩm} = \text{Giá kết thúc đấu giá} + \text{Chi phí giao nhận (nếu có)}$$

---

## 6. Hậu giao dịch & Đánh giá (Feedback & Rating)

Sau khi hoàn tất khâu thanh toán và nhận hàng, cả hai bên có quyền và nghĩa vụ đánh giá chất lượng:
- **Người mua đánh giá người bán:** Mức độ mô tả trung thực, thời gian giao hàng, thái độ phục vụ.
- **Người bán đánh giá người mua:** Thanh toán đúng hạn, tuân thủ cam kết giao dịch.

---

## 7. Yêu cầu phi chức năng & Bảo mật

- **Quản lý danh tính:** Người dùng bắt buộc phải đăng ký tài khoản và đăng nhập để đăng bán hoặc đấu giá.
- **Bảo mật & Mã hóa:** Tất cả dữ liệu giao dịch, thanh toán và thông tin nhạy cảm truyền qua mạng đều phải được **mã hóa (Encryption in transit & at rest)**.
