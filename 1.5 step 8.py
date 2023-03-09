class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.b = []


    def add(self, *a):
        c = []
        for i in a:
            c.append(i)
        self.b+=c
        while len(self.b) >= 5:
             print (self.b[0]+self.b[1]+self.b[2]+self.b[3]+self.b[4])
             del self.b[0]
             del self.b[0]
             del self.b[0]
             del self.b[0]
             del self.b[0]


    def get_current_part(self):
        return self.b
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены
buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]