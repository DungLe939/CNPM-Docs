#!/bin/bash
# Pre-commit check script cho Đồ án Nhập môn Công nghệ Phần mềm

# Tự động phát hiện đang chạy từ thư mục gốc Project hay từ thư mục cha Mon-hoc
if [ -d ".agents" ]; then
    PREFIX=""
else
    PREFIX="Introduction to Software Engineering/Project/"
fi

# Lấy danh sách các file đang được staged trong git
if [ -z "$PREFIX" ]; then
    STAGED_FILES=$(git diff --cached --name-only || true)
else
    STAGED_FILES=$(git diff --cached --name-only | grep "^${PREFIX}" || true)
    if [ -z "$STAGED_FILES" ]; then
        exit 0
    fi
fi

echo "====================================================================="
echo "🔍 [PRE-COMMIT HOOK] Đang kiểm tra thay đổi trong Đồ án CNPM..."
echo "====================================================================="

HAS_ERROR=0

# 1. Kiểm tra đường dẫn tuyệt đối máy tính cá nhân trong liên kết markdown [text](...) hoặc src/href
# Quét cả macOS (/Users/), Linux (/home/), và Windows (C:/ hoặc C:\)
if [ -z "$PREFIX" ]; then
    MD_DIFF=$(git diff --cached -U0 -- "*.md" "**/*.md" 2>/dev/null || true)
else
    MD_DIFF=$(git diff --cached -U0 -- "${PREFIX}"/**/*.md 2>/dev/null || true)
fi

# Phát hiện dạng ](/Users/...), ](file:///Users/...), ](C:...), src="/Users/..."
ABSOLUTE_LINKS=$(echo "$MD_DIFF" | grep -E '^\+.*(\]\((file:///Users/|/Users/|[a-zA-Z]:[/\\]|/home/)|(src|href)=["'"'"'](file:///Users/|/Users/|[a-zA-Z]:[/\\]|/home/))' || true)

if [ -n "$ABSOLUTE_LINKS" ]; then
    echo "❌ LỖI: Phát hiện liên kết tuyệt đối máy tính cá nhân trong tài liệu Markdown!"
    echo "$ABSOLUTE_LINKS"
    echo "   Quy tắc: Toàn bộ liên kết phải dùng đường dẫn tương đối (./ hoặc ../)."
    HAS_ERROR=1
fi

# 2. Kiểm tra nếu có sửa đổi trong .agents/skills/ mà chưa cập nhật .agents/README.md
SKILLS_CHANGED=$(echo "$STAGED_FILES" | grep "${PREFIX}\.agents/skills/" || true)
README_CHANGED=$(echo "$STAGED_FILES" | grep "${PREFIX}\.agents/README\.md" || true)

if [ -n "$SKILLS_CHANGED" ] && [ -z "$README_CHANGED" ]; then
    echo "⚠️  CẢNH BÁO: Bạn có thay đổi trong '.agents/skills/' nhưng chưa cập nhật '.agents/README.md'!"
    echo "   👉 Gợi ý: Hãy nhờ AI 'Cập nhật lại danh mục skills trong README.md'."
fi

# 3. Kiểm tra nếu có sửa đổi tài liệu tuần (docs/Week...) mà chưa cập nhật WEEKLY_TIMELINE.md
DOCS_CHANGED=$(echo "$STAGED_FILES" | grep "${PREFIX}docs/Week" || true)
TIMELINE_CHANGED=$(echo "$STAGED_FILES" | grep "${PREFIX}docs/WEEKLY_TIMELINE\.md" || true)

if [ -n "$DOCS_CHANGED" ] && [ -z "$TIMELINE_CHANGED" ]; then
    echo "⚠️  CẢNH BÁO: Bạn có tài liệu tuần mới trong 'docs/Week...' nhưng chưa cập nhật 'docs/WEEKLY_TIMELINE.md'!"
    echo "   👉 Gợi ý: Hãy nhờ AI 'Finalize tiến độ tuần và cập nhật timeline'."
fi

if [ $HAS_ERROR -ne 0 ]; then
    echo "---------------------------------------------------------------------"
    echo "⛔ Commit bị chặn do vi phạm quy tắc bắt buộc."
    echo "💡 Cách xử lý:"
    echo "   1. Nhờ AI: 'Sửa đường dẫn tuyệt đối thành tương đối giúp tôi'"
    echo "   2. Hoặc nếu muốn bỏ qua kiểm tra: git commit --no-verify"
    echo "====================================================================="
    exit 1
fi

echo "✅ Kiểm tra hợp lệ! Tiến hành commit..."
echo "====================================================================="
exit 0
