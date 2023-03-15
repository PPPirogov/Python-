
a=[]
with open('test_exercise.txt','r') as te:
    a = [line for line in te]
    #print (a)
with open('test_exercise.txt','w') as tw:
    for b in reversed(a):
        tw.write(b)
