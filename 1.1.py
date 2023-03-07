n = int(input())
if n <= 100 and n >=0:
    b = 1
    sum = 0
    while b <= n:
        a = int(input())
        sum += a
        b = b + 1
    print (sum)