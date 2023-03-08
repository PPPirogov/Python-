n = int(input())
ins = []
command=[]
finish = []
namespaces={"global": ["None", []]}
def find(space,var):
    b = namespaces[space]
    if var in b[1]:
        finish.append(space)
    elif space == "global" :
        finish.append('None')
        return 0
    else :
        c = namespaces[space]
        find(c[0], var)
        return 0

for i in range(n):
    ins =[]
    cmd, namesp, arg = input().split()
    ins.append(cmd)
    ins.append(namesp)
    ins.append(arg)
    command.append(ins)
    if cmd == 'add':
        b = namespaces[namesp]
        b[1].append(arg)
        namespaces[namesp] = b
        #print(namespaces)
    elif cmd == 'create':
        namespaces[namesp] = [arg,[]]
        #print(namespaces)
    elif cmd == 'get':
        find(namesp,arg)
        #print(namespaces)
#print (namespaces)

#print(command)
for a in finish:
    print(a)