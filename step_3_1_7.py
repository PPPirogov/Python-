s = 'aabababa'
t = 'aba'

# s = input()
# t = input()
# count_s = len(s)
# count_t = len(t)
len_raz = len(s)-len(t)
#print(count_s)
count = 0
number = 0
while count <= len_raz:
    #print(count, '  ', count+len(t))
    #print (s[count:count+len(t)])
    if s.find(t, count, count+len(t)) != -1:
        number += 1
    count += 1
print(number)
