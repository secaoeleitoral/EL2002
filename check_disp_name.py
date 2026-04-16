import re
with open('js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'function getCandidateDisplayName[\s\S]*?\}', text)
if match:
    print(match.group(0))
