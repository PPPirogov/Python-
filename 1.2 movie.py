x = [1,2,3,'dsad']
print (id(x))
print (id([1,2,3,'dsad']))

y = [1,2,3]
print (id(y))
print (id([1,2,3]))

z = [1,2,3,6]
s=z
z is s
s is [1,2,3,6]

p = [1,4,1]
q = p
q.append(3)
print (q)
print (p)