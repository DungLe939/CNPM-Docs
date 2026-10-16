# Quy tắc Nhắc nhở & Đồng bộ Drive Nhóm (Drive Sync Workflow Rule)

Tài liệu này là quy tắc ứng xử (Rule) bắt buộc dành cho AI khi làm việc với tài liệu nhóm trong dự án **Nhập môn Công nghệ Phần mềm**.

---

## 1. Nguyên tắc Kích hoạt & Nhắc nhở Chủ động (Proactive Reminder)

Người dùng và nhóm thường xuyên có các buổi họp và tải tài liệu mới lên Google Drive chung. Đôi khi người dùng có thể quên đồng bộ trước khi bắt đầu làm việc.

### Điều kiện AI Phải Chủ động Nhắc:
Khi người dùng đưa ra các yêu cầu như:
- *"Hôm nay làm docs tuần này nhé"*, *"Viết tiếp tài liệu tuần X"*, *"Phân tích biên bản họp"*
- *"Xem qua tài liệu nhóm mới gửi"*, *"Có tài liệu mới của nhóm đấy"*
- Hoặc mở đầu một buổi làm việc mới về đồ án sau một khoảng thời gian.

👉 **Hành động của AI:**
Trước khi thực hiện phân tích hoặc viết tài liệu, AI phải chủ động hỏi ngắn gọn:
> *"Trước khi bắt đầu, bạn có muốn mình kéo commit mới nhất từ GitHub (`git pull`) và đồng bộ tài liệu mới từ Google Drive về (`docs/Week01/`) không?"*

---

## 2. Quy trình Bắt buộc khi Người dùng Yêu cầu "Sync Drive"

Mỗi khi người dùng nói:
- *"sync drive"*, *"cập nhật drive"*, *"đồng bộ drive"*
- *"lấy tài liệu mới về"*, *"kéo biên bản họp về"*

### ⚠️ AI KHÔNG ĐƯỢC CHỈ TẢI DRIVE MÀ BỎ QUA GIT PULL.

Vì dự án có nhiều thành viên cùng làm việc trên GitHub, AI **BẮT BUỘC** thực hiện theo đúng thứ tự:

1. **Bước 1 (Git Pull):**
   - Chạy `git pull origin <current_branch>` để cập nhật mã nguồn và tài liệu mới nhất do đồng đội push lên GitHub.
   - Nếu có conflict, dừng lại và thông báo cho người dùng xử lý.

2. **Bước 2 (Drive Sync):**
   - Chạy `python3 .agents/scripts/sync_drive.py` để quét và tải các file mới hoặc file được chỉnh sửa từ thư mục Google Drive của nhóm về trực tiếp tài liệu tuần hiện tại (mặc định [docs/Week01/](../../docs/Week01/)).

3. **Bước 3 (Bắt buộc: Tự động Tóm tắt & Review Trực Tiếp Trên Đoạn Chat):**
   > ⚠️ **Quy tắc:** Toàn bộ nội dung tóm tắt và đánh giá **chỉ được viết trực tiếp trong tin nhắn chat** để người dùng đọc nhanh, **tuyệt đối không tự ý tạo file `.md` hay báo cáo phụ** gây rác repository.
   - Ngay sau khi file được tải về, AI **BẮT BUỘC** phải:
     1. **Tóm tắt cốt lõi:** Trích xuất các quyết định chính, thay đổi về kiến trúc, công nghệ, nhân sự hoặc deadline trong biên bản họp/tài liệu mới nhất.
     2. **Review & Đánh giá rủi ro (Critical Review):**
        - Đối chiếu với bối cảnh môn học ([docs/PROJECT_CONTEXT.md](../../docs/PROJECT_CONTEXT.md)) và tiến độ ([docs/WEEKLY_TIMELINE.md](../../docs/WEEKLY_TIMELINE.md)).
        - Đánh giá tính khả thi về kỹ thuật và khối lượng công việc (Scope creep) trong thời hạn đồ án (8 tuần).
        - Đưa ra cảnh báo rủi ro kỹ thuật (ví dụ: Voice AI thời gian thực, cào dữ liệu, tích hợp API...).
     3. **Đề xuất Action Items:** Liệt kê các đầu việc nhóm cần hành động ngay tiếp theo để người dùng nắm bắt trong phiên chat.

4. **Bước 4 (Bắt buộc: Rà soát Tính liên tục của Biên bản Họp):**
   - AI **phải đối chiếu tiến độ các buổi họp** (`Meeting_01`, `Meeting_02`, ...) với các cam kết hành động trong biên bản trước.
   - Nếu phát hiện có buổi họp theo lịch (ví dụ họp ngày 14/10 để chốt đề tài) nhưng thiếu file `Meeting_02.md`, AI **bắt buộc phải chủ động nhắc nhở trong chat** và đề xuất hỗ trợ tạo bản thảo chuẩn hóa dựa trên các quyết định thực tế.

---

## 3. Quy tắc Phân loại Thư mục Tự động (Auto-Classification)

Khi đồng bộ tài liệu, **tuyệt đối không lưu file lộn xộn ở thư mục gốc tuần (`docs/WeekXX/`)**. Hệ thống phải tự động phân loại:
- **Kế hoạch, Biên bản họp, Quyết định nhóm** (`Meeting_*.md`, `JobSeeker_Implementation_Plan.*`, `*Decision*`): $\rightarrow$ Bắt buộc lưu vào **`docs/WeekXX/Team_Decision_XX/`**.
- **Tài liệu học tập, Thông báo, Hướng dẫn, Biểu mẫu** (`Template*`, `Thông_báo_*`, `Material`): $\rightarrow$ Bắt buộc lưu vào **`docs/WeekXX/Material/`**.
- **Bài toán mẫu, Đặc tả mẫu** (`Problem_example_*`): $\rightarrow$ Bắt buộc lưu vào **`docs/WeekXX/Problem_example/`**.

---

## 4. Nghiêm cấm File Cache `.sync_manifest.json` trong Thư mục `docs/`

- File `.sync_manifest.json` là file cache metadata của script, **TUYỆT ĐỐI KHÔNG ĐƯỢC XUẤT HIỆN trong bất kỳ thư mục `docs/` nào**.
- Vị trí duy nhất: Ẩn tại `.agents/scripts/.sync_manifest.json` và đã được đưa vào `.gitignore`.
- Thư mục `docs/` chỉ được chứa tài liệu môn học sạch sẽ, ngăn nắp.

---

## 5. Tiện ích dành cho Thành viên Khác trong Nhóm

Nếu người dùng hỏi cách để các bạn trong nhóm tự chạy trên máy cá nhân mà không cần qua AI:
- Hướng dẫn chạy file tiện ích trong `.agents/scripts/`:
  ```bash
  ./.agents/scripts/sync.sh
  ```
  *(Lệnh này tự động thực hiện cả `git pull` và tải file mới từ Drive về, tự động phân loại vào các folder con tương ứng)*
