f = open('test.txt','r')
#x = f.readline(10)
#print(x)

# y = f.readline().rstrip()
# print(repr(y))
# y = y.splitlines()
# print(repr(y))
# y = f.readline()
# print(y)
# y = y.splitlines()
# print(repr(y))

x = f.readline()
print(repr(x))
for line in f:
    line=line.rstrip()
    print(repr(line))



f.close()