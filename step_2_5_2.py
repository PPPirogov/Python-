#x = input().split()
#print(x)
#map_obj = map(int,x) #2agrument: function and [a,b,c...] -> f(a),f(b),f(c)...
#n,k = (int(i) for i in x)

# print (map_obj)
# n=next(map_obj)
# k=next(map_obj)
#print(n+k)

#----------------------

x = input().split()
xs = (int(i) for i in x)

def even(x):
    return x%2 ==0
# evens = filter(even,xs)
# for i in evens:
#     print(i)
evens = list(filter(even,xs))
print(evens)