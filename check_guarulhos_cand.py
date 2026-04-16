import json
import re

with open('js/candidates.js', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'prefeito_1t.*?candidates\s*:\s*(\{.*?\})\s*\}\s*\},', text, re.DOTALL)
if match:
    # Look for how many code keys match our Guarulhos keys
    print("Candidates dict has Guarulhos 14, 20, 23, 43?")
    for k in ['13', '14', '20', '23', '43']:
        print(f"Key {k} present? : {k in match.group(1)}")
