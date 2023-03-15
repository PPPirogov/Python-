import os
import os.path


#os.chdir('.\main')
#print(os.getcwd())
substring = '.py'
answer_set = set()


for current_dir,dirs,files in os.walk('.\main'):
    for a in files:
        if substring in a:
            answer_set.add(current_dir)
            #print(current_dir)

# for a in answer:
#     print (a)
answer_list =[a for a in answer_set]
print (answer_set)
print (answer_list)
answer_list_with_t =[]
for a in answer_list:
    answer_list_with_t.append(a[2:])
answer_list_with_t.sort()
print (answer_list_with_t)
answer_list=[]
contents = '\n'.join(answer_list_with_t)
with open('answer_2_4_6.txt','w') as aw:
    for a in contents:
        aw.write(a)

txt = 'I like \\'
print(txt)
x = txt.replace('\\', '\*')

print(contents)
print(type(contents))