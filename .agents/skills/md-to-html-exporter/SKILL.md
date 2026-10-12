---
name: md-to-html-exporter
description: >-
  Kích hoạt khi người dùng yêu cầu chuyển đổi bài nộp Markdown (.md) sang HTML visualization (.html)
  với giao diện đẹp mắt, bảng biểu chuẩn và hỗ trợ in ấn theo quy định của giảng viên.
---

# MD TO HTML EXPORTER: XUẤT BÀI NỘP HTML VISUALIZATION

Giảng viên Thầy nndkhoa yêu cầu: **"bài nộp ở dạng markdown (md) kèm html (visualization của chính file md, có style và layout phù hợp)"**. Skill này cung cấp quy trình và công cụ để tạo file HTML hoàn chỉnh, đẹp mắt, có thể mở offline trên mọi trình duyệt.

---

## 1. Tiêu chuẩn của File HTML Visualization

1. **Tự chứa (Self-contained):** Chứa sẵn CSS hiện đại (kiểu GitHub Documentation / Technical Report), font chữ dễ đọc (liên kết Inter / Roboto hoặc system fonts), hỗ trợ dark/light mode hoặc in ấn sạch đẹp (A4 print layout).
2. **Hiển thị đầy đủ:**
   - Tiêu đề, phân cấp `h1`, `h2`, `h3` rõ ràng.
   - Bảng biểu có viền, sọc xen kẽ, căn chỉnh lề chuẩn.
   - Hỗ trợ công thức toán học MathJax/KaTeX (nếu có công thức tính phí).
   - Code block & Alert block nổi bật.

---

## 2. Quy trình Thực hiện

Khi người dùng yêu cầu chuyển đổi một file `.md` bất kỳ (ví dụ: `docs/Week02/Project_Proposal.md`) sang HTML:

### Cách 1: Sử dụng Script Python tích hợp (Khuyên dùng)
Dự án đã có sẵn script chuyển đổi tự động. Mở terminal tại **thư mục gốc `Project/`** và chạy:
```bash
# Chạy từ thư mục gốc Project/
python3 .agents/skills/md-to-html-exporter/scripts/render_md_to_html.py "docs/Week02/Project_Proposal.md"
```
File `.html` sẽ tự động được tạo cùng tên và cùng thư mục với file `.md` đầu vào.

### Cách 2: Biên tập trực tiếp cấu trúc HTML
Nếu không dùng script, nhúng nội dung HTML render từ Markdown vào khung mẫu sau:
```html
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Báo cáo Đồ án CNPM</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; max-width: 900px; margin: 40px auto; padding: 0 20px; color: #24292f; }
    h1, h2, h3 { color: #0969da; border-bottom: 1px solid #d0d7de; padding-bottom: 0.3em; }
    table { border-collapse: collapse; width: 100%; margin: 20px 0; }
    th, td { border: 1px solid #d0d7de; padding: 8px 12px; text-align: left; }
    th { background-color: #f6f8fa; }
    blockquote { border-left: 4px solid #0969da; margin: 0; padding-left: 16px; color: #57606a; }
    code { background-color: #afb8c133; padding: 0.2em 0.4em; border-radius: 6px; font-size: 85%; }
  </style>
</head>
<body>
  <!-- Nội dung chuyển đổi từ Markdown đặt tại đây -->
</body>
</html>
```
