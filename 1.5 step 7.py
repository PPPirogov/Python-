class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        self.v = v
        if self.v <= self.capacity:
            #print('yes')
            return True
        else:
            #print('no')
            return False
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        self.v = v
        if self.can_add(v) == True:
            self.capacity=self.capacity-self.v
            #print(self.capacity)
            return self.capacity
        else :
            return self.capacity

x = MoneyBox(15)
x.add(5)
x.add(9)
x.add(3)