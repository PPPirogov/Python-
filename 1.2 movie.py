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

x = [1, 2, 3]
y = x
y.append(4)

s = "123"
t = s
t = t + "4"
print(s)
print(t)
print(str(x) + " " + s)

s = 123
t = s
t *= 54
print(s)
print(t)


x=[1,2,3]
y=x
y=y*2
print(x)
#[1, 2, 3]
print(y)
#[1, 2, 3, 1, 2, 3]


x=[1,2,3]
y=x
y*=2
print(x)
#[1, 2, 3, 1, 2, 3]
print(y)
#[1, 2, 3, 1, 2, 3]

x=[1,2,3]
type(x)
type(4)
type(type(x))