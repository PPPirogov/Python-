import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
class LoggableList(Loggable,list):
    def append(self, x):
        super().append(x)
        self.log(x)
        return x

a = LoggableList()
a.append('msg 1')
a.append('msg 2')
print(a)