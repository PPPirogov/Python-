def list_sum(lst):
    result = 0
    for element in lst:
        result += element
    return result

def sum(a,b):
    return a+b
y = sum (12,323)
z = list_sum([1,34,43])
print (y)
print (z)

a = []

def foo(arg1, arg2):
    a.append("foo")
    a.append(arg1)

foo(23, a.append("arg2"))

print(a)