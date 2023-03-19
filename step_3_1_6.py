
# s = input()
# a = input()
# b = input()

s = 'aabbcc'
a = 'aa'
b = 'aaa'

count = 0
while count < 1000:
    if s.count(a) >= 1:
        s = s.replace(a, b)
        count += 1
        print(count)
        print(s)
    else:
        print(count)
        break
if count == 1000:
    print ('Impossible')