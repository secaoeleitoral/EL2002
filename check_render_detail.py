import re
with open('js/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_render_detail = False
for i, line in enumerate(lines):
    if 'function renderDetail' in line:
        in_render_detail = True
    if in_render_detail and 'info.nome' in line:
        print(f"Line {i+1}: {line.strip()}")
    if in_render_detail and line.strip().startswith('// ====='):
        in_render_detail = False
