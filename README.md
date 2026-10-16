# CNPM-Docs 📚

> **Không gian Quản lý Tài liệu, Biên bản Họp & Hệ thống Trợ lý AI Đồ án**  
> Môn học: **Nhập môn Công nghệ Phần mềm** (SE) — GVTH: **Thầy nndkhoa**

---

## 📌 Điều hướng Nhanh (Quick Links)

- 📋 **[PROJECT_CONTEXT.md](./docs/PROJECT_CONTEXT.md):** Bối cảnh đồ án, quy chuẩn kỹ thuật và các mốc thời gian quan trọng.
- ⏱️ **[WEEKLY_TIMELINE.md](./docs/WEEKLY_TIMELINE.md):** Nhật ký theo dõi tiến độ từng tuần, trạng thái deliverables và link bài nộp.
- 🤖 **[.agents/README.md](./.agents/README.md):** Danh mục AI Skills, Rules ứng xử và tự động hóa Pre-commit.

---

## 📂 Cấu trúc Repository

```text
CNPM-Docs/
├── README.md                           # Trang chủ dự án & điều hướng
├── .gitignore                          # Cấu hình bỏ qua file rác (OS, Office temp, IDE...)
├── Template#0-ProjectProposal-2022.docx# Biểu mẫu Project Proposal chuẩn bộ môn
├── docs/                               # Toàn bộ tài liệu đồ án
│   ├── PROJECT_CONTEXT.md              # Bối cảnh & quy chế môn học
│   ├── WEEKLY_TIMELINE.md              # Nhật ký tiến độ từng tuần
│   ├── Week01/                         # Kế hoạch chi tiết, tài liệu & biên bản tuần 1
│   └── Week02/                         # Chuẩn bị Project Proposal đợt 1
└── .agents/                            # Trung tâm vận hành AI & Tự động hóa
    ├── README.md                       # Danh mục kỹ năng AI (Skills Catalog)
    ├── rules/                          # Quy tắc ứng xử (Drive-sync, Pre-commit workflow...)
    ├── scripts/                        # Scripts tự động hóa (sync_drive.py, sync.sh...)
    └── skills/                         # Các kỹ năng chuyên biệt cho AI
```

---

## 🔄 Hướng dẫn Đồng bộ Tài liệu (Dành cho Thành viên Nhóm)

Thư mục Google Drive chung của nhóm được đồng bộ trực tiếp vào tài liệu tuần hiện tại (mặc định [docs/Week01/](./docs/Week01/)).

### Cách 1: Tự động 100% khi Mở VS Code / Cursor (Zero-effort)
Repo đã được cài sẵn tính năng tự động chạy ngầm:
- **Khi vừa mở thư mục dự án:** Tự động chạy `git pull --rebase --autostash origin main` để cập nhật tài liệu mới nhất từ đồng đội mà không làm gián đoạn hay mất các dòng bạn đang viết dở.
- **Trong khi làm việc:** Cứ mỗi 2 phút, editor sẽ tự động kiểm tra xem có ai vừa push tài liệu mới lên GitHub không và hiển thị thông báo dưới thanh Status Bar.

> 💡 **Lưu ý lần đầu:** Nếu VS Code hiện thông báo *"Allow Automatic Tasks in Folder"*, hãy bấm **Allow and Run** để kích hoạt.

### Cách 2: Chạy 1 Lệnh Tắt trong Terminal (Đồng bộ cả Git lẫn Google Drive)
Chỉ cần mở Terminal tại thư mục dự án và chạy:
```bash
./.agents/scripts/sync.sh
```
Lệnh này sẽ tự động:
1. Chạy `git pull origin` để lấy các commit mới nhất từ đồng đội trên GitHub.
2. Quét và tải các biên bản họp/tài liệu mới nhất từ Google Drive về đúng thư mục tuần tương ứng (không tải lại các file đã có).

### Cách 3: Nhờ AI thực hiện
Nếu làm việc trong IDE cùng AI, chỉ cần nhắn:
> *"Cập nhật Drive đi"* hoặc *"Sync drive"*
AI sẽ tự động thực hiện cả 2 bước trên, đọc lướt các tài liệu mới và tự động tóm tắt, review chuyên sâu cho bạn.

---

## ⚡ Quy ước Làm việc cho Nhóm (Guidelines)

1. **Quy tắc Vàng về Đường dẫn:** Luôn sử dụng **đường dẫn tương đối (`./`, `../`)** trong mọi tài liệu Markdown để tránh lỗi khi đồng bộ giữa các máy tính.
2. **Quy trình Trước khi Commit:**
   - Khi nhờ AI hoàn thành công việc, AI sẽ tự động kích hoạt rule `pre-commit-workflow` để cập nhật `WEEKLY_TIMELINE.md` và kiểm tra liên kết.
   - Nếu commit thủ công bằng Terminal, script Git Pre-commit Hook sẽ tự động rà soát và cảnh báo nếu có lỗi.
3. **Phân cấp Tài liệu:**
   - Các file ghi chép thô, chưa biên tập đặt hậu tố `_raw.md`.
   - File chính thức hoàn chỉnh đặt theo PascalCase hoặc kebab-case.
