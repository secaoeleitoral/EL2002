import re
with open('js/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'info.nome' in line:
        print(f"{i+1}: {line.strip()}")
