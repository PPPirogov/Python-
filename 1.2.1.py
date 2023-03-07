n = int(input())
objects = []
mn = set()
if n <= 100 and n >=0:
    b = 1
    while b <= n:
        a = int(input())
        objects.append(a)
        b = b + 1
    for a in objects:
        mn.add(a)
    print (len(mn))



