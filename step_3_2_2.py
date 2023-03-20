import re
#print(re.match)
#print(re.search)
#print(re.findall)
#print(re.sub)

#[] -- можно указать множество подходящих символов
# . ^ $ * + ? { } [ ] \ | ( ) -- метасимволы
# \d - [0-9] - цифры
# \D - [^0-9] - не цифры
# \s - [ \t\n\r\f\v] -- пробельные символы
# \S - [^ \t\n\r\f\v]
# \w - [a-zA-Z0-9_] --буквы + цифры + _
# \W - [^a-zA-Z0-9_]

pattern = r'a.c'
#pattern = r'a[\w.]c'
#pattern = r'a[a-zA-Z]c'
#pattern = r'a[^a-zA-Z]c'
string = 'acc'
match_object = re.search(pattern,string)
print (match_object)

string = 'abc, a.c, aac,adc,a-c,aZc'
all_inclusions = re.findall(pattern,string)
print(all_inclusions)

fixed_typos = re.sub(pattern,'abc',string)
print(fixed_typos)
