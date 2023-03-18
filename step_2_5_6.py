def f(x):
  def f1(y):
    return y+x
  return f1

a=f(5)
print(a)
print(a(2))