import re

pattern = r' english?'
string = 'Do you speak english?'
match = re.search(pattern, string)

print(match)

pattern = r' english\?'
match = re.search(pattern, string)
print(match)