def g():
    print("Funcion G")
    return 10
def f():
    print("Funcion F")
    g()
    print("Funcion F")
print ("I'm outside of any funcion")
f()
print ("I'm outside of any funcion")

x = [1,2,3]
x.append(g())
x.append(5)
print(x)
top = x.pop()
print (top)
print(x)
top = x.pop()
print (top)
print(x)