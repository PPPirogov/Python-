class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0
class MyList(list,EvenLengthMixin):
    pass
class MyDict(dict,EvenLengthMixin):
    pass

x= MyDict()
x["key"]= "value"
x["Another key"] = "Another value"
print(x.even_length())