import re
with open('js/candidates.js', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'prefeito_1t\s*:\s*\{[^}]*candidates\s*:\s*\{([^}]*)\}', text, re.DOTALL)
if match:
    # Just print the first 20 lines of the candidates block
    print(match.group(1)[:500])
else:
    print("Not found prefeito_1t. Keys in CANDIDATES:")
    keys = re.findall(r'(\w+)\s*:\s*\{\s*label', text)
    print(keys)
