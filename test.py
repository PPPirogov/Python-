import sys, re
pattern = r'(cat)'
for line in sys.stdin:
    line = line.rstrip()
    all_inclusions = re. search(r"cat\b", line)
    print(all_inclusions)
    #print(count(all_inclusions))
    #if len(all_inclusions) >= 2:
        #print(line)