# HỆ THỐNG SKILLS CHO AI (`.agents/`)

> Thư mục này chứa bộ kỹ năng chuẩn hóa (Skills) dành cho các trợ lý AI (Gemini, Claude, GPT, Cursor, v.v.) trong đồ án môn học **Nhập môn Công nghệ Phần mềm** (GVTH: Thầy nndkhoa).

---

## 1. Tổng quan Danh mục Skills

Hiện tại dự án đã trang bị **5 kỹ năng chuyên biệt** được đặt trong thư mục `./skills/`:

| STT | Tên Skill | Đường dẫn | Khi nào AI tự động kích hoạt? | Nhiệm vụ chính |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **`project-navigator`** | [./skills/project-navigator/SKILL.md](./skills/project-navigator/SKILL.md) | Khi cần tra cứu cấu trúc dự án, tìm kiếm vị trí tài liệu tuần, kiểm tra tiến độ. | Cung cấp bản đồ thư mục, kết nối với [PROJECT_CONTEXT.md](../docs/PROJECT_CONTEXT.md) và [WEEKLY_TIMELINE.md](../docs/WEEKLY_TIMELINE.md). |
| **2** | **`se-proposal-writer`** | [./skills/se-proposal-writer/SKILL.md](./skills/se-proposal-writer/SKILL.md) | Khi người dùng yêu cầu soạn thảo, chỉnh sửa hoặc hoàn thiện Project Proposal. | Hướng dẫn AI viết đúng 5 mục của biểu mẫu bộ môn, khống chế 1-2 trang sơ lược, lập bảng User Stories và kiến trúc. |
| **3** | **`anti-ai-fluff`** | [./skills/anti-ai-fluff/SKILL.md](./skills/anti-ai-fluff/SKILL.md) | Khi rà soát, kiểm tra văn phong tài liệu kỹ thuật trước khi nộp. | Cung cấp danh sách từ cấm (Blacklist) và checklist loại bỏ triệt để dấu hiệu AI Writing sáo rỗng để tránh bị trừ điểm nặng. |
| **4** | **`project-utility`** | [./skills/project-utility/SKILL.md](./skills/project-utility/SKILL.md) | Khi thao tác với file, tạo liên kết, định dạng bảng biểu hoặc đồng bộ tiến độ. | Thực thi quy tắc vàng: **Ưu tiên đường dẫn tương đối (relative paths)**, liên kết kép (Dual-Linking), chuẩn hóa đặt tên file và cập nhật timeline. |
| **5** | **`drive-sync`** | [./skills/drive-sync/SKILL.md](./skills/drive-sync/SKILL.md) | Khi cần đồng bộ Drive, kéo biên bản họp hoặc tài liệu nhóm mới. | Tự động hóa luồng 2 bước: `git pull origin` $\rightarrow$ tải file mới từ Google Drive về [docs/Week01/](../docs/Week01/) và tóm tắt, review. |

---

## 2. Cách AI Tương tác với Hệ thống Skills

1. **Nhận diện tự động:** Khi bạn đặt câu hỏi trong phiên chat, AI sẽ quét qua phần YAML frontmatter (`name` và `description`) của từng file `SKILL.md` để quyết định kích hoạt skill tương ứng.
2. **Tiết kiệm ngữ cảnh (Token-efficient):** AI chỉ đọc nội dung chi tiết của một skill khi tác vụ thực sự yêu cầu, giúp phản hồi luôn nhanh và chính xác.
3. **Tương thích đa nền tảng:**
   - Hoạt động native trên **Antigravity IDE** với Gemini.
   - Có thể dùng làm tham chiếu chỉ dẫn (System Instructions) cho các AI khác như Claude Code, Cursor, Copilot hoặc ChatGPT.

---

## 3. Quy tắc Bắt buộc cho Tất cả Skills

> **"Nếu được, hãy sử dụng đường dẫn tương đối (relative paths) nhiều nhất có thể."**

Mọi tài liệu, liên kết và tham chiếu bên trong thư mục `.agents/` và toàn bộ dự án phải luôn dùng đường dẫn tương đối (`./`, `../`) để đảm bảo không bị lỗi khi đồng bộ Git trên các máy tính khác nhau.

---

## 4. Hệ thống Quy tắc Ứng xử (Rules) & Kiểm duyệt Tự động

Thư mục `./rules/` chứa các quy tắc bắt buộc áp dụng trong toàn bộ vòng đời phát triển:

- **[drive-sync-workflow.md](./rules/drive-sync-workflow.md):** Quy định AI **chủ động nhắc nhở đồng bộ Drive** khi bắt đầu làm tài liệu, và **bắt buộc chạy `git pull` trước khi kéo file từ Drive** để tránh xung đột giữa các thành viên.
- **[pre-commit-workflow.md](./rules/pre-commit-workflow.md):** Quy định AI **phải tự động finalize docs & skills** trước khi thực hiện commit. Các bước bao gồm:
  1. Đồng bộ `docs/WEEKLY_TIMELINE.md`.
  2. Cập nhật `README.md` của `.agents/` nếu có kỹ năng mới.
  3. Quét kiểm tra đường dẫn tương đối và lọc văn phong AI sáo rỗng (`anti-ai-fluff`).
  4. Tạo commit theo chuẩn Conventional Commits.

---

## 5. Tích hợp Git Pre-commit Hook

Dự án trang bị script kiểm tra tự động tại `./scripts/pre_commit_check.sh`:
- Được kích hoạt tự động qua hook `.git/hooks/pre-commit` mỗi khi bạn gõ `git commit`.
- Chỉ quét các thay đổi trong đồ án CNPM (không làm ảnh hưởng các môn học khác trong repository).
- Tự động chặn commit nếu phát hiện đường dẫn tuyệt đối máy tính cá nhân (`/Users/...`).
- Nhắc nhở người dùng khi có tài liệu tuần mới hoặc skill mới mà quên cập nhật timeline và README.
