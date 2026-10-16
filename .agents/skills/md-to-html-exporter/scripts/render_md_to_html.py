#!/usr/bin/env python3
import sys
import os
import re

CSS_STYLE = """
:root {
  --color-primary: #0969da;
  --color-text: #24292f;
  --color-bg: #ffffff;
  --color-border: #d0d7de;
  --color-subtle-bg: #f6f8fa;
  --color-muted: #57606a;
}
@media (prefers-color-scheme: dark) {
  :root {
    --color-primary: #58a6ff;
    --color-text: #c9d1d9;
    --color-bg: #0d1117;
    --color-border: #30363d;
    --color-subtle-bg: #161b22;
    --color-muted: #8b949e;
  }
}
* { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  line-height: 1.65;
  color: var(--color-text);
  background-color: var(--color-bg);
  max-width: 960px;
  margin: 40px auto;
  padding: 0 24px;
}
h1, h2, h3, h4 {
  color: var(--color-primary);
  font-weight: 600;
  margin-top: 1.5em;
  margin-bottom: 0.5em;
  border-bottom: 1px solid var(--color-border);
  padding-bottom: 0.3em;
}
h1 { font-size: 2rem; }
h2 { font-size: 1.5rem; }
h3 { font-size: 1.25rem; }
p, ul, ol { margin-top: 0.5em; margin-bottom: 1em; }
li { margin-bottom: 0.3em; }
a { color: var(--color-primary); text-decoration: none; }
a:hover { text-decoration: underline; }
table {
  border-collapse: collapse;
  width: 100%;
  margin: 1.5em 0;
  font-size: 0.95em;
}
th, td {
  border: 1px solid var(--color-border);
  padding: 10px 14px;
  text-align: left;
}
th {
  background-color: var(--color-subtle-bg);
  font-weight: 600;
}
tr:nth-child(even) {
  background-color: var(--color-subtle-bg);
}
blockquote {
  border-left: 4px solid var(--color-primary);
  margin: 1em 0;
  padding: 8px 16px;
  background-color: var(--color-subtle-bg);
  color: var(--color-muted);
  border-radius: 0 4px 4px 0;
}
code {
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
  background-color: var(--color-subtle-bg);
  border: 1px solid var(--color-border);
  padding: 0.2em 0.4em;
  border-radius: 4px;
  font-size: 85%;
}
pre code {
  display: block;
  padding: 16px;
  overflow-x: auto;
  font-size: 90%;
  border-radius: 6px;
}
hr {
  border: 0;
  height: 1px;
  background: var(--color-border);
  margin: 2em 0;
}
@media print {
  body { max-width: 100%; margin: 0; padding: 20mm; background: #fff; color: #000; }
  h1, h2, h3 { color: #000; }
  table, tr, td, th { border-color: #999; }
}
"""

def simple_markdown_to_html(md_text):
    # Remove frontmatter
    md_text = re.sub(r'^---\n.*?\n---\n', '', md_text, flags=re.DOTALL)
    
    # Check if python-markdown or mistune or commonmark is available
    try:
        import markdown
        return markdown.markdown(md_text, extensions=['tables', 'fenced_code', 'toc'])
    except ImportError:
        pass
        
    # Check for fenced code blocks including mermaid
    # Replace ```mermaid ... ``` with <pre class="mermaid">...</pre>
    def replace_code_blocks(match):
        lang = match.group(1).strip().lower() if match.group(1) else ''
        code = match.group(2)
        if lang == 'mermaid':
            return f'<div class="mermaid-container" style="background:#fff;padding:16px;border-radius:8px;border:1px solid var(--color-border);margin:20px 0;text-align:center;"><pre class="mermaid">{code.strip()}</pre></div>'
        else:
            escaped_code = code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            return f'<pre><code>{escaped_code.strip()}</code></pre>'

    # Process fenced code blocks before splitting lines
    code_block_pattern = r'```([a-zA-Z0-9_-]*)\n(.*?)```'
    placeholders = {}
    
    def save_block(m):
        idx = f"__CODE_BLOCK_{len(placeholders)}__"
        placeholders[idx] = replace_code_blocks(m)
        return idx
        
    md_text = re.sub(code_block_pattern, save_block, md_text, flags=re.DOTALL)

    lines = md_text.split('\n')
    html_lines = []
    in_table = False
    
    for line in lines:
        stripped = line.strip()
        
        if stripped in placeholders:
            if in_table:
                html_lines.append("</tbody></table>")
                in_table = False
            html_lines.append(placeholders[stripped])
            continue
            
        # Headers
        if stripped.startswith('# '):
            html_lines.append(f"<h1>{stripped[2:]}</h1>")
        elif stripped.startswith('## '):
            html_lines.append(f"<h2>{stripped[3:]}</h2>")
        elif stripped.startswith('### '):
            html_lines.append(f"<h3>{stripped[4:]}</h3>")
        elif stripped.startswith('#### '):
            html_lines.append(f"<h4>{stripped[5:]}</h4>")
        elif stripped.startswith('---'):
            html_lines.append("<hr>")
        elif stripped.startswith('> '):
            html_lines.append(f"<blockquote><p>{stripped[2:]}</p></blockquote>")
        elif stripped.startswith('- ') or stripped.startswith('* '):
            html_lines.append(f"<li>{stripped[2:]}</li>")
        elif '|' in stripped and stripped.startswith('|') and stripped.endswith('|'):
            cells = [c.strip() for c in stripped.strip('|').split('|')]
            if all(re.match(r'^:?-+:?$', c) for c in cells):
                continue  # separator line
            if not in_table:
                in_table = True
                html_lines.append("<table><thead><tr>")
                for c in cells:
                    html_lines.append(f"<th>{c}</th>")
                html_lines.append("</tr></thead><tbody>")
            else:
                html_lines.append("<tr>")
                for c in cells:
                    html_lines.append(f"<td>{c}</td>")
                html_lines.append("</tr>")
        else:
            if in_table:
                html_lines.append("</tbody></table>")
                in_table = False
            if stripped:
                html_lines.append(f"<p>{stripped}</p>")
                
    if in_table:
        html_lines.append("</tbody></table>")
        
    res = '\n'.join(html_lines)
    # Bold & Italic & inline code
    res = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', res)
    res = re.sub(r'\*(.+?)\*', r'<em>\1</em>', res)
    res = re.sub(r'`(.+?)`', r'<code>\1</code>', res)
    return res

def render_file(input_path):
    if not os.path.exists(input_path):
        print(f"Error: File not found: {input_path}")
        sys.exit(1)
        
    with open(input_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
        
    title_match = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', md_content, re.MULTILINE)
    title = title_match.group(1) if title_match else os.path.splitext(os.path.basename(input_path))[0]
    
    body_html = simple_markdown_to_html(md_content)
    
    html_output = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <!-- MathJax for formulas -->
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <!-- Mermaid.js for Diagrams -->
  <script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize({{ startOnLoad: true, theme: 'default', securityLevel: 'loose' }});
  </script>
  <style>
{CSS_STYLE}
  </style>
</head>
<body>
  {body_html}
</body>
</html>"""

    output_path = os.path.splitext(input_path)[0] + '.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_output)
        
    print(f"Successfully generated HTML visualization: {output_path}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 render_md_to_html.py <input.md>")
        sys.exit(1)
    render_file(sys.argv[1])
