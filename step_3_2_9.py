import sys, re
pattern = r'\\'
for line in sys.stdin:
    line = line.rstrip()
    all_inclusions = re.search(pattern, line)
    if all_inclusions:
        print(line)