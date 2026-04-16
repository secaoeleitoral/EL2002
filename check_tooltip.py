import re
with open('js/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'tooltip' in line.lower() or 'popup' in line.lower() or 'mouse' in line.lower():
        print(f"{i+1}: {line.strip()}")
