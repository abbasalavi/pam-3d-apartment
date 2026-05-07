c = open('index.html', 'r', encoding='utf-8').read()
import re
matches = re.findall(r"['\"](\w+\.\w+)['\"]", c)
for m in sorted(set(matches)):
    print(m)
