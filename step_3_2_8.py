import sys, re
pattern = r'(cat)'
for line in sys.stdin:
    line = line.rstrip()
    all_inclusions = re. findall(r"cat\b", line)
    #print(type(all_inclusions))
    #print(count(all_inclusions))
    if len(all_inclusions) >= 2:
        print(line)