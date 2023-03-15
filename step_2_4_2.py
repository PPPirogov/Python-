x = open('test_write','w')
# x.write('Hello\n')
# x.write(' World')

lines =['line1','line2','line 3']
contents = '\n'.join(lines)
x.write(contents)

x.close()

f = open('test_append','a')
f.write('hello\n')

f.close()