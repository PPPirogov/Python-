# def f (x,y):
#     try :
#         return x/y
#     except TypeError:
#         print ('Type Error')
#     except ZeroDivisionError:
#         print('Zero division: y = 0')
#
# print (f(5,'dsad'))

# def f (x,y):
#     try :
#         return x/y
#     except (TypeError,ZeroDivisionError) as e:
#         print ('Error')
#         print (type(e))
#         print(e)
#         print(e.args)
#     except ZeroDivisionError:
#         print('Zero division: y = 0')
#
# print (f(5,0))
# print (f(5,[]))


try :
    25/0
    #e
except ArithmeticError: #isinstance(e,ArithmeticError) ==  True
    print ('ArithmeticError')
except ZeroDivisionError:  # isinstance(e,ZeroDivisionError) ==  True
    print('ZeroDivisionError')
print (ArithmeticError.mro())