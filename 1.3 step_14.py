def fib(x):
    if x == 0 or x ==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)
print (fib(15))
print (fib(16))
print (fib(17))