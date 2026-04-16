import json
import re

with open('js/candidates.js', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'prefeito_1t.*?candidates\s*:\s*(\{.*?\})\s*\}\s*\},', text, re.DOTALL)
if match:
    print(match.group(1))

