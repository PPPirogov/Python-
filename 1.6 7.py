import sys
sys.stdin = open("input.txt", "r")
d={}
n = int(input())
i = 0
d = {}

for i in range(n):
    key, *value = input().split()
    d[key] = value
mas = []
q = int(input())
for b in d:
    a = d[b]
    if ':' in a:
        a.remove(':')
    d[b] = a
    #print (d[b])
print (d)
for element in range(0, q):
    mas.append(input().split())
print (mas)

def search(iskom,*parent):
    print(iskom)
    print(parent)
    val = False
    if iskom in parent:
        val = True
        print("yes")
    else:
        print('d[iskom]: ',d[iskom])
        if d[iskom] in parent:
            val = True



search('D','B')