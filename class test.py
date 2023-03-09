class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.b = [32,3213,3213,3123,323]


    def add(self, *a):
        print(self.b)
        len(self.b)
        print(a)
        c = []
        for i in a:
            c.append(i)
        print(c)
        self.b +=c
        print(self.b)
        while len(self.b) >= 5:
            print (print (self.b[0]+self.b[1]+self.b[2]+self.b[3]+self.b[4]))
            self.b = []

buf = Buffer()
buf.add(1, 2, 3)