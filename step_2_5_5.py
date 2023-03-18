from functools import partial
import operator as op

x = int("110101",base=2)
print(x)
int_2 = partial(int,base=2)
y = int_2("110101")
print (y)

y = [
    ('Gfad','dsa','Cra'),
    ('Tesa','Aewe'),
    ('jon','Backq')
]

sort_by_last = partial(list.sort,key = op.itemgetter(-1))
print(y)
sort_by_last(y)
print(y)

a = ['zbd','fda','abb']
sort_by_last(a)
print(a)