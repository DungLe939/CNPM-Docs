---
name: anti-ai-fluff
description: >-
  Kích hoạt khi rà soát, biên tập và kiểm tra văn phong tài liệu kỹ thuật trước khi nộp
  nhằm loại bỏ triệt để các dấu hiệu văn phong AI (AI Writing, sáo rỗng, tô vẽ).
---

# ANTI AI FLUFF: LOẠI BỎ VĂN PHONG AI WRITING

Giảng viên Thầy nndkhoa đã đưa ra cảnh báo: **"Các dấu hiệu của AI Writing cần được loại bỏ trước khi nộp... Vi phạm bị TRỪ ĐIỂM RẤT NẶNG"**. Skill này cung cấp quy tắc và checklist bắt buộc để rà soát văn bản.

---

## 1. Danh sách từ ngữ & Mẫu câu cấm (Blacklist)

Khi phát hiện các mẫu câu sau trong tài liệu, phải loại bỏ hoặc viết lại ngay:

### 1.1. Mẫu câu mở đầu sáo rỗng

| Mẫu câu AI điển hình | Vấn đề | Cách sửa |
| :--- | :--- | :--- |
| *"Trong kỷ nguyên số 4.0 / thời đại công nghệ..."* | Mở bài cliché, không có giá trị thông tin | Bỏ câu này, đi thẳng vào mô tả hệ thống |
| *"Trong bối cảnh hiện nay / ngày nay..."* | Câu đệm rỗng, lặp đi lặp lại ở mọi bài AI | Xóa, viết thẳng: *"Hệ thống X giải quyết bài toán Y..."* |
| *"Với sự phát triển mạnh mẽ / không ngừng của..."* | Sáo ngữ mở đầu đặc trưng AI tiếng Việt | Bỏ toàn bộ câu mở đầu này |

### 1.2. Tính từ & Cụm từ hoa mỹ vô nghĩa

| Mẫu câu AI điển hình | Vấn đề | Cách sửa |
| :--- | :--- | :--- |
| *"Đóng vai trò vô cùng quan trọng / thiết yếu..."* | Tính từ thổi phồng, không đo lường được | Nêu tác động cụ thể: *"Giảm 40% thời gian xử lý đơn hàng"* |
| *"Một bước đột phá mang tính cách mạng..."* | Quảng cáo, không phải văn phong kỹ thuật | Nêu công nghệ: *"Sử dụng WebSocket để truyền dữ liệu thời gian thực"* |
| *"Hệ thống toàn diện, tối ưu, mạnh mẽ, linh hoạt..."* | Xếp chồng tính từ chung chung | Thay bằng đặc tả: *"API đáp ứng độ trễ dưới 200ms với 1000 concurrent users"* |
| *"Trải nghiệm tuyệt vời / hoàn hảo / vượt trội..."* | Đánh giá chủ quan, vô căn cứ | Bỏ hoặc thay bằng tiêu chí UX cụ thể |
| *"Nhằm nâng cao / góp phần xây dựng..."* | Cụm từ đệm AI hay chèn vào cuối câu | Viết thẳng hành động: *"Hệ thống cho phép người dùng..."* |

### 1.3. Cấu trúc câu đặc trưng AI

| Mẫu câu AI điển hình | Vấn đề | Cách sửa |
| :--- | :--- | :--- |
| *"Không chỉ... mà còn..."* | Cấu trúc nhấn mạnh giả tạo | Viết ngắn: *"Hệ thống hỗ trợ A và B"* |
| *"Đáp ứng mọi nhu cầu / giải pháp toàn diện..."* | Cam kết quá mức, phi thực tế | Liệt kê chức năng cụ thể thay vì khái quát hóa |
| *"Từ đó / Qua đó / Nhờ vậy mà..."* (lặp nhiều lần) | Liên từ lặp mẫu — dấu hiệu AI rõ ràng | Giảm thiểu liên từ, tách thành câu đơn độc lập |
| *"Được thiết kế với mục tiêu / Được xây dựng nhằm..."* | Câu bị động lặp mẫu (passive pattern) | Đổi sang chủ động: *"Nhóm xây dựng module X để..."* |

---

## 2. Dấu hiệu Cấu trúc AI (Structural Red Flags)

Ngoài từ ngữ, AI còn để lại dấu vết qua **cách tổ chức nội dung**:

1. **Liệt kê 3 bullet đều bắt đầu cùng cấu trúc ngữ pháp:**
   - ❌ *"Hệ thống hỗ trợ... / Hệ thống cho phép... / Hệ thống cung cấp..."* (3 câu liên tiếp cùng chủ ngữ + động từ)
   - ✅ Thay đổi cách diễn đạt, đan xen chủ động / bị động / câu danh từ.

2. **Đoạn văn quá cân xứng:**
   - ❌ Mỗi mục đều có đúng 3 dòng, đều có 1 câu mở + 2 gạch đầu dòng.
   - ✅ Nội dung thực tế hiếm khi đối xứng hoàn hảo. Cho phép độ dài không đều.

3. **Lặp từ khóa quá nhiều trong 1 đoạn:**
   - ❌ Từ *"người dùng"* xuất hiện 5 lần trong 3 câu liên tiếp.
   - ✅ Dùng đại từ (*"họ"*), hoặc rút gọn (*"sau khi đăng nhập, hệ thống hiển thị..."*).

---

## 3. 5 Quy tắc Viết Kỹ thuật Phần mềm (SE Writing Rules)

1. **Quy tắc Trực diện (Directness):**
   - Viết câu đơn hoặc câu ghép ngắn (dưới 25 từ).
   - Vào thẳng chủ ngữ - vị ngữ - hành động cụ thể.
   - Bỏ mọi câu mở đầu dạng *"Như chúng ta đã biết..."*.

2. **Quy tắc Định lượng (Quantification):**
   - Thay vì *"hệ thống xử lý nhanh"*, hãy viết: *"thời gian phản hồi dưới 500ms"*.
   - Thay vì *"bảo mật cao"*, hãy viết: *"mã hóa mật khẩu bằng bcrypt, truyền tải qua HTTPS/TLS 1.3"*.

3. **Quy tắc Bảng biểu & Sơ đồ (Tables & Diagrams):**
   - Thay vì mô tả dài dòng bằng 5 đoạn văn, hãy chuyển thành 1 bảng biểu so sánh hoặc ma trận trách nhiệm.

4. **Quy tắc Đúng giới hạn (Scope Confinement):**
   - Không đưa vào các nội dung chưa được yêu cầu trong tuần hiện tại.
   - Ở tài liệu Proposal: Không viết Use Case Spec chi tiết 10 trang; chỉ viết tóm tắt User Story ngắn gọn.

5. **Quy tắc Giọng văn Chủ động (Active Voice):**
   - Hạn chế tối đa câu bị động (*"được thiết kế", "được xây dựng", "được triển khai"*).
   - Ưu tiên: *"Nhóm thiết kế module X"*, *"Hệ thống lưu trữ dữ liệu vào PostgreSQL"*.

---

## 4. Checklist Tự Đánh giá trước khi Nộp

### 4.1. Rà soát Từ ngữ
- [ ] Tài liệu có câu mở đầu dạng *"Trong bối cảnh / kỷ nguyên / ngày nay..."* không? → Xóa ngay.
- [ ] Các tính từ mơ hồ (*tuyệt vời, hoàn hảo, tối ưu hóa triệt để, toàn diện*) đã thay bằng thông số kỹ thuật cụ thể chưa?
- [ ] Có cụm từ *"đóng vai trò quan trọng"*, *"góp phần nâng cao"*, *"đáp ứng mọi nhu cầu"* nào còn sót không?

### 4.2. Rà soát Cấu trúc
- [ ] Có 3+ bullet points liên tiếp bắt đầu bằng cùng cấu trúc ngữ pháp không? → Viết lại đa dạng.
- [ ] Có đoạn văn nào dùng quá 3 câu bị động liên tiếp không? → Đổi sang chủ động.
- [ ] Từ *"người dùng"* hoặc *"hệ thống"* có lặp quá 3 lần trong cùng 1 đoạn không? → Rút gọn hoặc dùng đại từ.

### 4.3. Rà soát Phạm vi
- [ ] Báo cáo có vượt quá dung lượng yêu cầu của đợt nộp không? (Proposal: tối đa 5-7 trang, phần nghiệp vụ chỉ 1-2 trang).
- [ ] Có nội dung nào thuộc về đợt nộp sau (ví dụ: chi tiết Use Case, Sequence Diagram ở tuần Proposal) không? → Loại bỏ.
- [ ] Thuật ngữ chuyên ngành đã dùng đúng chuẩn tiếng Anh kỹ thuật (Client, Server, Database, Cache, API) chưa?
