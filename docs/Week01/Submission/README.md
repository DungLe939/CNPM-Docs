# HỒ SƠ BÀI NỘP ĐỢT 1: PROJECT PROPOSAL (P1)

> **Môn học:** Nhập môn Công nghệ Phần mềm  
> **GVTH:** Thầy Nguyễn Ngô Duy Khoa (`nndkhoa`)  
> **Thời gian giao bài:** 12/10/2026  
> **Đơn vị thực hiện:** Nhóm 02 (4 sinh viên - Trưởng nhóm: Lê Tấn Dũng)  

---

## 📦 1. Thành phần Hồ sơ Bài nộp trong Thư mục

Thư mục này chuẩn bị sẵn **đầy đủ bộ đôi bắt buộc** theo quy chế của giảng viên:

| Tên tệp tin | Định dạng | Mô tả nội dung |
| :--- | :---: | :--- |
| **[`Project_Proposal.md`](./Project_Proposal.md)** | Markdown | Toàn văn bản đề xuất đồ án đợt 1 chuẩn 5 phần theo biểu mẫu bộ môn, đáp ứng đủ 6 tiêu chí *"Chọn Project Idea Nhanh"*, mô hình Scrum 8 tuần. |
| **[`Project_Proposal.html`](./Project_Proposal.html)** | HTML Visualization | Bản trực quan hóa rendered từ file `.md`, có stylesheet CSS hiện đại, responsive, tích hợp render Mermaid diagrams trực tiếp. |

---

## 📌 2. Hướng dẫn Đóng gói & Đặt tên Tệp tin Nộp bài (Theo Lời Thầy Dặn)

### Quy định của Giảng viên:
1. **Thành phần nộp:** 01 file `.md` và 01 file `.html` visualization của chính file `.md`.
2. **Hình thức nộp:** Đóng gói thành **01 tệp nén duy nhất định dạng `.zip`**.
3. **Quy tắc đặt tên file `.zip`:**
   ```text
   Nhom02-MSSV1-MSSV2-MSSV3-MSSV4.zip
   ```
   *Ví dụ:* `Nhom02-24120001-24120002-24120003-24120004.zip`
4. **Đại diện nộp:** **Chỉ 01 thành viên duy nhất nộp** đại diện cho cả nhóm (Trưởng nhóm: Lê Tấn Dũng).

---

## ⚡ 3. Lệnh Terminal để Đóng gói Nhanh File ZIP

Khi đã cập nhật đầy đủ MSSV thực tế vào file, bạn chỉ cần mở terminal tại thư mục này và chạy lệnh:

```bash
# Thay thế các MSSV bằng thông tin thực tế của nhóm:
zip -j "Nhom02-MSSV1-MSSV2-MSSV3-MSSV4.zip" Project_Proposal.md Project_Proposal.html
```

*(Tham số `-j` giúp nén trực tiếp 2 file mà không bị dính đường dẫn thư mục lồng nhau, rất tiện cho thầy mở chấm).*

---

## ✅ 4. Checklist Tự Kiểm tra Trước Khi Bấm Nộp

- [x] Đã xác định số thứ tự nhóm: **Nhóm 02**
- [ ] Đã thay thế các placeholder `<MSSV1>`, `<MSSV2>`, `<MSSV3>`, `<MSSV4>` bằng MSSV thật chưa?
- [ ] File `.zip` đã chứa đúng 02 file: `Project_Proposal.md` và `Project_Proposal.html` chưa?
- [ ] Đã mở thử file `Project_Proposal.html` trên trình duyệt xem giao diện, bảng biểu và sơ đồ có hiển thị chuẩn đẹp chưa?
- [ ] Tên file `.zip` đã đúng định dạng `Nhom02-MSSV1-MSSV2-MSSV3-MSSV4.zip` chưa?
- [ ] Đã cử đúng 01 bạn (Trưởng nhóm) nộp lên hệ thống chưa?
