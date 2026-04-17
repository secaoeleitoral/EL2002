import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find and print context around the problematic area
for i, line in enumerate(lines):
    if '}an>' in line or ('renderCandidateCards' in line and i > 325 and i < 340):
        print(f'{i+1}: {repr(line)}')

# Remove the garbled line and the duplicate block following it
# The bad line looks like: "    }an>`).join('');\n"
# then two blank lines and the duplicate renderMetrics/renderCandidateCards/}
output = []
skip_next = 0
i = 0
while i < len(lines):
    if skip_next > 0:
        skip_next -= 1
        i += 1
        continue
    line = lines[i]
    if '}an>' in line:
        # Skip this line and check if next few are the duplicate renderMetrics block
        # Skip: this line, blank, blank, renderMetrics, renderCandidateCards, }
        skip_next = 5
        i += 1
        continue
    output.append(line)
    i += 1

with open('js/app.js', 'w', encoding='utf-8') as f:
    f.writelines(output)
print('Done. Lines removed.')
