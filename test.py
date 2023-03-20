import sys, re
pattern = r'z...z'
for line in sys.stdin:
    line = line.rstrip()
    all_inclusions = re.search(pattern, line)
    #print(all_inclusions)
    if all_inclusions:
        print(line)
    #print(count(all_inclusions))
    #if len(all_inclusions) >= 2:
        #print(line)