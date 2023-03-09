class Counter:
    def __init__(self,start = 20):
        self.count = start


x = Counter(10)
x1 = Counter ()
print(x.count)
print(x1.count)
x.count +=1