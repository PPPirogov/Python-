import sys, re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'(\w+)\1'
    match = re.match(pattern,line)
    print(line)
    print (match)
    if match:
        print(line)

