class ExtendedStack(list):
    def sum(self):
        op1, op2 = self.pop(), self.pop()
        self.append(op1 + op2)

    def sub(self):
        # операция вычитания
        op1, op2 = self.pop(), self.pop()
        self.append(op1 - op2)
    def mul(self):
        # операция умножения
        op1, op2 = self.pop(), self.pop()
        self.append(op1 * op2)
    def div(self):
        # операция целочисленного деления
        op1, op2 = self.pop(), self.pop()
        self.append(op1 // op2)


ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
print (ex_stack)
ex_stack.div()
print (ex_stack)
assert ex_stack.pop() == 2
print (ex_stack)
ex_stack.sub()
print (ex_stack)
assert ex_stack.pop() == 6
print (ex_stack)
ex_stack.sum()
print (ex_stack)
assert ex_stack.pop() == 7
print (ex_stack)
ex_stack.mul()
print (ex_stack)
assert ex_stack.pop() == 2
print (ex_stack)
assert len(ex_stack) == 0
print (ex_stack)


print (ex_stack)