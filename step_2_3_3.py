from random import random

class RandomIterator:
    def __iter__(self):
        return self
    def __init__(self,k):
        self.k = k
        self.i = 0
    def __next__(self):
        if self.i < self.k:
            self.i+=1
            return random()
        else:
            raise StopIteration
# x = RandomIterator(3)
# iter(x)
# for x in RandomIterator(10):
#     print (x)

# def random_generator(k):
#     for i in range(k):
#         yield random()
#
# a = random_generator(3)
#
# for i in a:
#     print(i)
# print (type(a))
# print (a)
#
def simple_gen():
    print('Checkpoint1')
    yield 1
    print('Checkpoint2')
    return 3
    yield 2
    print('Checkpoint3')

gen = simple_gen()
x = next(gen)
print(x)
y = next(gen)
print(y)
z = next(gen)
#print(z)