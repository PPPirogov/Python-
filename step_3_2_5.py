import re

#pattern = r'text'
pattern = r'((abc)|(test|text)*)'
string = 'textexttest'
match = re.match(pattern, string)
print(match)
print(match.groups())
print('')
########################################

pattern = r'Hello (abc|test)'
string = 'Hello abc'
match = re.match(pattern, string)
print(match)
print(match.group(0))
print(match.group(1))

print('')
########################################

pattern = r'(\w+)-\1'
#string = 'test-text'
string = 'test-test chow-chow'
#match = re.match(pattern,string)
#print(match)
duplicates = re.sub(pattern, r'\1', string)
print (duplicates)

print('')
########################################

pattern = r'((\w+)-\2)'
#string = 'test-text'
string = 'test-test chow-chow'
#match = re.match(pattern,string)
#print(match)
duplicates = re.findall(pattern, string)
print (duplicates)
