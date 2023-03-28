import sys, re

for line in sys.stdin:
    line = line.rstrip()
    duplicates = re.sub("human","computer",line)
    print(duplicates)