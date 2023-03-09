# class Counter:
#     x = 0
# Counter
# x = Counter()
# x.count =0
# x.count+=1
# v = 2
# print(type(Counter))
# print(type(x))
# print(type(x.count))
# print(type(v))

class Counter:
  x = 0
  print('Counter created!')

c1 = Counter()
c2 = Counter()
c2.x += 1
Counter.y = 789

print(c1.x)
print(c2.x)
print(c2.y)
print(c1.y)