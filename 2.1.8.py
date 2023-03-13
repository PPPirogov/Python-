def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise ValueError(name+ ' is inappropriate name')

# print(greet('Anton'))
# print(greet('anton'))

while True:
    try:
        name  = input("Please enter your name: ")
        getting = greet(name)
        print(getting)
    except ValueError:
        print("Please ty again")
    else:
        break