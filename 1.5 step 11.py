class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1


a = A()
b = A()
print(a.val)
print(b.val)

a.bar()
a.foo()
print(a.val)
print(b.val)

c = A()

print(a.val)
print(b.val)
print(c.val)