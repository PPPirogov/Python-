def print_a_lot_of_argument(a,b,*korteg):
    print (a)
    print (b)
    for i in korteg:
        print(i)

#print_a_lot_of_argument(1,2,4,5,62,2,1,'dsad','dsa')

def print_kwargs(a,b,**kwargs):
    print (a)
    print (b)
    for i in kwargs:
        print(i,kwargs[i])

print_kwargs (10,e=1,d=4,r=7,b=1)