import re

pattern = r'ab?a' # 0 или 1 вхождение
#pattern = r'ab*a' #если нет b, есть b 1,2,3 или сколько угодно раз
#pattern = r'ab+a' #есть b 1,2,3 или сколько угодно раз
#pattern = r'ab(2,4)a' # 2 или 4 вхождение

string = 'aa, aba, abba, abbba, abbba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)
print(' ')

#pattern1 = r'a[ab]+a'
pattern1 = r'a[ab]+?a'
string1 = 'abaaba'
the_most_long = re.match(pattern1, string1)
print(the_most_long)
print(re.match(pattern1, string1))
print(re.findall(pattern1, string1))

