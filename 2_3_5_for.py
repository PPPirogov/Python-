x = [-2,-1,0,1,2,4]
y = [i*i for i in x if i>0]
print(y)

x = [(a,b) for a in range(3) for b in range(4) if b>=a ]
print (x)

z = ((a,b) for a in range(3) for b in range(4) if b>=a )
print (z)
print (next(z))
print (next(z))

a = [i + 1 for i in range(4)]
print (a)

a = [i for i in range(5)][1:]
print (a)