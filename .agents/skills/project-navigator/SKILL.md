---
name: project-navigator
description: >-
  Kích hoạt khi cần tra cứu cấu trúc dự án, tìm kiếm vị trí các tài liệu tuần,
  kiểm tra tiến độ môn học, hoặc xác định ngữ cảnh môn Nhập môn Công nghệ Phần mềm.
---

# PROJECT NAVIGATOR: BẢN ĐỒ ĐỊNH VỊ DỰ ÁN

Skill này giúp AI hiểu ngay cấu trúc tổ chức file và tiến độ hiện tại của đồ án mà không mất thời gian tìm kiếm hoặc hỏi lại người dùng.

## 1. Nguồn dữ liệu cốt lõi (Single Source of Truth)

Trước khi thực hiện bất kỳ tác vụ nào liên quan đến môn học, AI luôn tham khảo 2 file sau:
- [docs/PROJECT_CONTEXT.md](../../../docs/PROJECT_CONTEXT.md): Chứa toàn bộ thông tin môn học, giảng viên, mục tiêu đồ án và các quy định bắt buộc (format nộp bài, cấm AI writing sáo rỗng).
- [docs/WEEKLY_TIMELINE.md](../../../docs/WEEKLY_TIMELINE.md): Ghi nhận chi tiết tuần hiện tại nhóm đang làm gì, thành phẩm cần nộp và kế hoạch các tuần tiếp theo.

## 2. Bản đồ Thư mục & Mục đích sử dụng

```text
Project/
├── Template#0-ProjectProposal-2022.docx / .pdf  # Template Proposal chuẩn bộ môn
├── docs/
│   ├── PROJECT_CONTEXT.md      # Tổng quan dự án, môn học & quy định GV
│   ├── WEEKLY_TIMELINE.md      # Nhật ký tiến độ từng tuần
│   ├── Week01/                 # Tài liệu & hoạt động tuần 1
│   │   ├── text1.md            # Thông báo chính thức từ GVTH Thầy nndkhoa
│   │   ├── Problem_example/    # Các bài toán đặc tả mẫu (Sàn đấu giá, Health monitor)
│   │   │   ├── Problem_example_01.md & _raw.md
│   │   │   └── Problem_example_02.md & _raw.md
│   │   └── Team_Decision_01/   # Biên bản họp nhóm, ý tưởng đề tài tuần 1
│   └── Week02/ (Sắp tới)       # Đợt nộp Proposal đợt 1
└── .agents/
    ├── README.md               # Mô tả tổng quan & danh mục tất cả skills, rules
    ├── rules/                  # Quy tắc ứng xử bắt buộc (Pre-commit workflow...)
    ├── scripts/                # Script tự động hóa (Pre-commit check hook...)
    └── skills/                 # Hệ thống kỹ năng hỗ trợ đồ án
```

## 3. Quy tắc Định vị & Đặt tên File

Khi tạo file hoặc thư mục mới cho đồ án, luôn tuân thủ nguyên tắc:
1. **Phân cấp theo tuần:** Đặt trong `docs/Week<XX>/` tương ứng với tuần học.
2. **File thô vs File chuẩn hóa:** 
   - Văn bản gốc chưa chỉnh sửa đặt hậu tố `_raw.md`.
   - Tài liệu kỹ thuật chuẩn hóa đặt tên theo PascalCase hoặc kebab-case (`Project_Proposal.md`, `Software_Specification.md`).
3. **Luôn cập nhật Timeline:** Bất cứ khi nào hoàn thành hoặc bắt đầu một đợt nộp, cập nhật ngay vào `docs/WEEKLY_TIMELINE.md`.
