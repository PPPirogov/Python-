x = [
    ('Gfad','dsa','fre'),
    ('Tesa','Qewe'),
    ('jon','Back')
]

# def length(name):
#     return len(' '.join(name))
# name_lengths = [length(name) for name in x]
# print (name_lengths)
# x.sort(key=length)
x.sort(key = lambda name:len(' '.join(name)))

print(x)