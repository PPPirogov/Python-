import re

pattern = r'ab?a' # 0 или 1 вхождение
#pattern = r'ab*a' #если нет b, есть b 1,2,3 или сколько угодно раз
#pattern = r'ab+a' #есть b 1,2,3 или сколько угодно раз
#pattern = r'ab(2,4)a' # 2 или 4 вхождение

string = 'aa, aba, abba, abbba, abbba'
all_inclusions = re.findall(pattern,string)
print(all_inclusions)