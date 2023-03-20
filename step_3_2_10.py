import sys, re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'(\w+)\1\b'
    match = re.match(pattern,line)
    if match:
        print(line)