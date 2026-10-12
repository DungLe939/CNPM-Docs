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
│   ├── Week01/                         # Tài liệu, đề bài mẫu & biên bản tuần 1
│   └── Week02/                         # Chuẩn bị Project Proposal đợt 1
└── .agents/                            # Trung tâm vận hành AI
    ├── README.md                       # Danh mục kỹ năng AI (Skills Catalog)
    ├── rules/                          # Quy tắc ứng xử (Pre-commit workflow...)
    ├── scripts/                        # Scripts tự động hóa kiểm tra
    └── skills/                         # Các kỹ năng chuyên biệt cho AI
```

---

## ⚡ Quy ước Làm việc cho Nhóm (Guidelines)

1. **Quy tắc Vàng về Đường dẫn:** Luôn sử dụng **đường dẫn tương đối (`./`, `../`)** trong mọi tài liệu Markdown để tránh lỗi khi đồng bộ giữa các máy tính.
2. **Quy trình Trước khi Commit:**
   - Khi nhờ AI hoàn thành công việc, AI sẽ tự động kích hoạt rule `pre-commit-workflow` để cập nhật `WEEKLY_TIMELINE.md` và kiểm tra liên kết.
   - Nếu commit thủ công bằng Terminal, script Git Pre-commit Hook sẽ tự động rà soát và cảnh báo nếu có lỗi.
3. **Phân cấp Tài liệu:**
   - Các file ghi chép thô, chưa biên tập đặt hậu tố `_raw.md`.
   - File chính thức hoàn chỉnh đặt theo PascalCase hoặc kebab-case.
