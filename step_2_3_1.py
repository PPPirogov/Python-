lst = [1,2,3,4,5]
book = {'title':'The Langoliers',
        'autor':'Stephen King',
        'years_published':1990}
string = 'Hello world'

iterator = iter(book)
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))

#for i in string:
#    print (i)
it = iter(book)
while True:
    try:
        i=next(it)
        print(i)
    except StopIteration:
        break