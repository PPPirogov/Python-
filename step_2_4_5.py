import os.path
print(os.getcwd())
print(os.listdir('.idea'))

print(os.path.exists('dbnavigator.xml'))
print(os.path.exists('1.1.py'))

print(os.path.isfile('dbnavigator.xml'))
print(os.path.isfile('1.1.py'))

print(os.path.isdir('dbnavigator.xml'))
print(os.path.isdir('simplecrypt'))

print(os.path.abspath('tests.py'))
os.chdir('.idea')
print(os.getcwd())