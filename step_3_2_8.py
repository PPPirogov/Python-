import sys, re
pattern = r'\bcat\b'
for line in sys.stdin:
    line = line.rstrip()
    all_inclusions = re.search(pattern, line)
    if all_inclusions:
        print(line)
    #print(count(all_inclusions))
    #if len(all_inclusions) >= 2:
        #print(line)