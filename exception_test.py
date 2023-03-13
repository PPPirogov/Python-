GREETING = 'HELLO'
_GREETING = 'HELLO'

class BadName:
    pass

def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise ValueError(name+ ' is inappropriate name')
print('Import is execution')

#__all__=['BadName','greet']
# print(greet('Anton'))
# print(greet('anton'))

# while True:
#     try:
#         name  = input("Please enter your name: ")
#         getting = greet(name)
#         print(getting)
#     except ValueError:
#         print("Please ty again")
#     else:
#         break