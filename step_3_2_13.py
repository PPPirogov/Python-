import sys, re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'\b(a+)\b'
    duplicates = re.sub(pattern,"argh",line,1,re.IGNORECASE)
    print(duplicates)