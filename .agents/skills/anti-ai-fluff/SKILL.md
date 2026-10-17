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

4. **Lạm dụng dấu chấm phẩy (`;`) trong câu văn & bảng biểu (Punctuation Red Flag):**
   - ❌ *"Khảo sát thực tế; bóc tách câu chuyện người dùng; phân rã Product Backlog; xây dựng sơ đồ..."* (Lỗi AI điển hình: Dùng `;` để nối chuỗi hành động hoặc ngăn cách các ý trong câu văn xuôi, tạo cảm giác máy móc, lai tạp ngữ pháp tiếng Anh hoặc câu lệnh code).
   - ✅ **Quy tắc bắt buộc:** 
     - Thay thế dấu chấm phẩy (`;`) bằng dấu phẩy (`,`) khi liệt kê các thành phần hoặc vế câu song song cùng cấp.
     - Tách thành các câu đơn độc lập có dấu chấm (`.`) nếu mỗi vế là một mệnh đề hoàn chỉnh (có chủ ngữ - vị ngữ riêng).
     - Tuyệt đối không để dấu chấm phẩy (`;`) xuất hiện tràn lan trong các ô bảng biểu, các gạch đầu dòng mô tả tính năng hay câu văn xuôi.

5. **Lỗi viết hoa tùy tiện danh từ chung (Random Capitalization / Title Case Red Flag):**
   - ❌ *"ghi nhận trạng thái vào Nhật ký ứng tuyển"*, *"tính toán Điểm tương thích"*, *"hiển thị Bảng phân tích khoảng cách kỹ năng"*, *"xuất bản Báo cáo Đánh giá Năng lực"* (Lỗi AI điển hình: Tự tiện viết hoa chữ cái đầu của danh từ chung ở giữa câu do dịch máy hoặc bắt chước kiểu viết hoa Title Case của tiếng Anh).
   - ✅ **Quy tắc bắt buộc:** 
     - **Chỉ viết hoa:** Đầu câu sau dấu chấm, tên người, tên địa danh (*Hồ Chí Minh*, *Hà Nội*), tên cơ quan/trường học (*Trường ĐH Khoa học Tự nhiên*), tên sản phẩm riêng (*HireUS*, *SeekerBot*), và các từ viết tắt kỹ thuật (*CV*, *JD*, *ATS*, *API*, *SMTP*, *AI*, *IT*, *PDF*, *JWT*).
     - **Bắt buộc viết thường** mọi danh từ chung, tên chức năng, loại bảng biểu hoặc khái niệm khi nằm giữa câu: *"nhật ký ứng tuyển"*, *"điểm tương thích năng lực"*, *"bảng phân tích khoảng cách kỹ năng"*, *"báo cáo đánh giá năng lực"*, *"thư ứng tuyển"*, *"phòng phỏng vấn ảo"*.

6. **Lạm dụng dấu ngoặc đơn `(...)` để chêm chú thích và dịch thuật song ngữ (Parentheses Overuse Red Flag):**
   - ❌ *"kết nối sinh viên ngành Công nghệ Thông tin (chuyên ngành Kỹ thuật Phần mềm, Khoa học Máy tính...)"*, *"thực tập sinh (Intern) và mới tốt nghiệp (Fresher)"*, *"thư ứng tuyển (Cover Letter)"*, *"hạn chót nộp hồ sơ (deadline)"*, *"gửi thư rác (spam)"*, *"dội âm (Echo)"*, *"thiết bị người dùng (Client)"*. (Lỗi AI điển hình: Mở ngoặc đơn liên tục sau các danh từ để dịch song ngữ Anh - Việt hoặc chêm phụ chú vụn vặt, khiến câu văn bị phân mảnh, đứt gãy nhịp đọc và lộ rõ dấu hiệu dịch máy).
   - ✅ **Quy tắc bắt buộc:**
     - **Hạn chế tối đa mở ngoặc đơn `(...)`:** Chỉ dùng ngoặc đơn khi thực sự cần thiết, như đưa ví dụ minh họa ngắn gọn mang tính điển hình (*"trang cá nhân (LinkedIn, GitHub)"*, *"độ phân giải từ 1280 x 720 (HD) trở lên"*).
     - **Không kẹp kè dịch song ngữ Anh - Việt trong ngoặc đơn:** Chọn một thuật ngữ phù hợp nhất để dùng nhất quán trong câu văn xuôi (dùng *"thực tập sinh và fresher"*, *"thư ứng tuyển"*, *"hạn chót nộp hồ sơ"*, *"gửi thư rác"*, *"phía client"*, *"phía server"*).
     - **Hòa nhập phần chú thích vào dòng văn tự nhiên:** Thay vì *"thông tin học vấn (trường, chuyên ngành, điểm GPA tích lũy, chứng chỉ chuyên môn)"*, hãy diễn đạt mạch lạc bằng từ nối: *"thông tin học vấn gồm trường, chuyên ngành, điểm GPA tích lũy và chứng chỉ chuyên môn"*.

7. **Lỗi liệt kê tên tệp cộc lốc thay vì mô tả sản phẩm (Raw Filename Drop Red Flag):**
   - ❌ *"Thành phẩm: Project_Proposal.md và Project_Proposal.html"*, *"Deliverables: SRS.md, SDD.md, Test_Report.md"*.
   - **Vấn đề:** Liệt kê tên file cộc lốc khiến người đọc không chuyên (non-tech), người chấm điểm hoặc thành viên mới gia nhập dự án không thể hiểu được sản phẩm đó là gì, chứa nội dung gì và giải quyết bài toán gì.
   - ✅ **Quy tắc bắt buộc:** Luôn mô tả rõ ràng bản chất và nội dung cốt lõi của sản phẩm trước. Giải thích sản phẩm đó làm được gì, chứa đựng những thành phần nào bằng ngôn ngữ trực quan, dễ hiểu (tên file kỹ thuật chỉ đóng vai trò tham chiếu phụ đi kèm).

8. **Lỗi tự tiện bịa số liệu cam kết chưa được kiểm chứng (Unverified Metric Commitment Red Flag):**
   - ❌ *"Phản hồi dưới 1.5s"*, *"Độ trễ API dưới 200ms"*, *"Tổng chi phí là 0 VNĐ"*, *"Hỗ trợ 10.000 người dùng đồng thời"*.
   - **Vấn đề:** Tự tiện đưa các con số định lượng cụ thể, cứng nhắc vào tài liệu đề xuất (Proposal) khi nhóm chưa đo lường thực nghiệm hoặc chưa chốt phương án. Đến lúc triển khai thực tế nếu không đạt được hoặc có chi phí phát sinh sẽ bị trừ điểm nặng hoặc thất bại khi nghiệm thu.
   - ✅ **Quy tắc bắt buộc:** Tuyệt đối không tự tiện bịa số liệu kỹ thuật hay tài chính. Khi chưa có số liệu đo đạc chính thức, phải diễn đạt an toàn ở mức định hướng/mục tiêu dự kiến (*"tối ưu hóa tốc độ tải trang"*, *"dự toán chi phí dự kiến ưu tiên sử dụng các gói miễn phí Free Tier"*).

---

## 3. 8 Quy tắc Viết Kỹ thuật Phần mềm (SE Writing Rules)

1. **Quy tắc Trực diện (Directness):**
   - Viết câu đơn hoặc câu ghép ngắn (dưới 25 từ).
   - Vào thẳng chủ ngữ - vị ngữ - hành động cụ thể.
   - Bỏ mọi câu mở đầu dạng *"Như chúng ta đã biết..."*.

2. **Quy tắc Định lượng có kiểm chứng (Verified Quantification):**
   - Chỉ định lượng bằng con số cụ thể khi số liệu đó đã được kiểm chứng thực nghiệm hoặc được nhóm/người dùng chính thức chốt.
   - Tuyệt đối không tự bịa các con số cứng (thời gian, chi phí 0 VNĐ) vào tài liệu đề xuất sơ bộ.
   - Nêu rõ giải pháp kỹ thuật cụ thể thay vì thổi phồng: *"mã hóa mật khẩu bằng bcrypt, truyền tải qua HTTPS/TLS 1.3"* thay vì *"bảo mật cao"*.

3. **Quy tắc Bảng biểu & Sơ đồ (Tables & Diagrams):**
   - Thay vì mô tả dài dòng bằng 5 đoạn văn, hãy chuyển thành 1 bảng biểu so sánh hoặc ma trận trách nhiệm.

4. **Quy tắc Đúng giới hạn (Scope Confinement):**
   - Không đưa vào các nội dung chưa được yêu cầu trong tuần hiện tại.
   - Ở tài liệu Proposal: Không viết Use Case Spec chi tiết 10 trang; chỉ viết tóm tắt User Story ngắn gọn.

5. **Quy tắc Giọng văn Chủ động (Active Voice):**
   - Hạn chế tối đa câu bị động (*"được thiết kế", "được xây dựng", "được triển khai"*).
   - Ưu tiên: *"Nhóm thiết kế module X"*, *"Hệ thống lưu trữ dữ liệu vào PostgreSQL"*.

6. **Quy tắc Dấu câu Tự nhiên (Natural Punctuation):**
   - Dùng dấu phẩy (`,`) để ngắt các vế câu hoặc liệt kê các danh từ/cụm từ cùng cấp.
   - Dùng dấu chấm (`.`) để kết thúc một mệnh đề hoàn chỉnh, tạo nhịp điệu dứt khoát.
   - **Tuyệt đối không lạm dụng dấu chấm phẩy (`;`)** trong văn xuôi và bảng biểu; chỉ dùng trong code hoặc các cú pháp lập trình chuyên biệt.

7. **Quy tắc Viết hoa Chuẩn Tiếng Việt (Vietnamese Capitalization Rule):**
   - **Không viết hoa tùy tiện danh từ chung** ở giữa câu để "nhấn mạnh" tính năng hoặc rập khuôn kiểu Title Case tiếng Anh.
   - Viết thường toàn bộ các cụm từ: *nhật ký ứng tuyển*, *điểm tương thích*, *bảng phân tích kỹ năng*, *báo cáo năng lực*, *thư ứng tuyển*, *phòng phỏng vấn ảo*, *bảng điều khiển*...
   - Chỉ viết hoa chữ cái đầu câu, danh từ riêng (tên người, địa danh, tên trường, tên sản phẩm thương hiệu) và từ viết tắt kỹ thuật.

8. **Quy tắc Tiết chế Dấu ngoặc đơn (Parentheses Restraint Rule):**
   - Tránh việc mở ngoặc đơn liên tiếp trong cùng một câu văn.
   - Không dùng ngoặc đơn để dịch song ngữ từ ngữ thông dụng.
   - Chỉ dùng ngoặc đơn khi thực sự cần thiết (ví dụ dẫn nguồn tài liệu tham khảo, đưa ví dụ minh họa tiêu biểu hoặc quy đổi đơn vị đo lường).

---

## 4. Checklist Tự Đánh giá trước khi Nộp

### 4.1. Rà soát Từ ngữ
- [ ] Tài liệu có câu mở đầu dạng *"Trong bối cảnh / kỷ nguyên / ngày nay..."* không? → Xóa ngay.
- [ ] Các tính từ mơ hồ (*tuyệt vời, hoàn hảo, tối ưu hóa triệt để, toàn diện*) đã thay bằng thông số kỹ thuật cụ thể chưa?
- [ ] Có cụm từ *"đóng vai trò quan trọng"*, *"góp phần nâng cao"*, *"đáp ứng mọi nhu cầu"* nào còn sót không?

### 4.2. Rà soát Cấu trúc & Dấu câu
- [ ] Có 3+ bullet points liên tiếp bắt đầu bằng cùng cấu trúc ngữ pháp không? → Viết lại đa dạng.
- [ ] Có đoạn văn nào dùng quá 3 câu bị động liên tiếp không? → Đổi sang chủ động.
- [ ] Từ *"người dùng"* hoặc *"hệ thống"* có lặp quá 3 lần trong cùng 1 đoạn không? → Rút gọn hoặc dùng đại từ.
- [ ] **Kiểm tra dấu câu:** Đã rà soát và thay thế triệt để các dấu chấm phẩy (`;`) trong văn xuôi và bảng biểu bằng dấu phẩy (`,`) hoặc tách thành câu đơn có dấu chấm (`.`) chưa?
- [ ] **Kiểm tra viết hoa:** Đã rà soát và đưa toàn bộ các danh từ chung bị viết hoa tùy tiện ở giữa câu (*"Nhật ký"*, *"Điểm tương thích"*, *"Bảng phân tích"*, *"Báo cáo"*...) về chữ thường chuẩn tiếng Việt chưa?
- [ ] **Kiểm tra dấu ngoặc đơn:** Đã rà soát và loại bỏ việc lạm dụng dấu ngoặc đơn `(...)` để dịch song ngữ Anh - Việt hoặc chêm phụ chú rườm rà chưa? (Chỉ giữ lại các ngoặc đơn thực sự cần thiết như dẫn ví dụ tiêu biểu).
- [ ] **Kiểm tra mô tả sản phẩm đầu ra:** Đã rà soát và loại bỏ việc liệt kê tên file cộc lốc (.md, .html...)? Đảm bảo mọi thành phẩm đều được mô tả rõ ràng về bản chất, nội dung và giá trị thực tế để người ngoài ngành (non-tech) và người mới tham gia dự án hiểu được ngay chưa?

### 4.3. Rà soát Phạm vi
- [ ] Báo cáo có vượt quá dung lượng yêu cầu của đợt nộp không? (Proposal: tối đa 5-7 trang, phần nghiệp vụ chỉ 1-2 trang).
- [ ] Có nội dung nào thuộc về đợt nộp sau (ví dụ: chi tiết Use Case, Sequence Diagram ở tuần Proposal) không? → Loại bỏ.
- [ ] Thuật ngữ chuyên ngành đã dùng đúng chuẩn tiếng Anh kỹ thuật (Client, Server, Database, Cache, API) chưa?
