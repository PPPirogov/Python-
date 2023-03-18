import operator as op

print(op.add(4,5))
print(op.mul(4,5))
print(op.contains([1,2,3],4))

# x=[1,2,3]
# f = op.itemgetter(1) #f(x) == x[1]
x= {'123':'first_element','234':'Second_element','245':'tird_element'}
f = op.itemgetter('123') #f(x) == x['123']

print (f(x))

y = [
    ('Gfad','dsa','Cra'),
    ('Tesa','Aewe'),
    ('jon','Backq')
]

y.sort(key=op.itemgetter(-1))
print(y)