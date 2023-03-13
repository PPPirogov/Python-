class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError()

        else:
            super().append(x)

x = PositiveList([3,4,8,-5,0,8])
x.append(1)
x.append(2)
#x.append(0)
#x.append(-8)
x.append(7)

print(x)