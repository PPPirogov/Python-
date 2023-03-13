def dividi(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Division by zero")
    else:
        print ('result is' , result)
    finally:
        print('finally')
dividi(2,1)
dividi(2,0)
dividi(2,[])
