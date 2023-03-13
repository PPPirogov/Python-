class B():
    def method(self):
        print('Not')

class C(B):
    def method(self):
        super().method()
        print('Bad')
x = C()
x.method()