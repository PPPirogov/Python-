import sys, re
pattern = r'z...z'
for line in sys.stdin:
    line = line.rstrip()
    all_inclusions = re.search(pattern, line)
    if all_inclusions:
        print(line)