import requests
number =[]

with open('number.txt','r') as te:
    for a in te:
        a=a.rstrip()
        number.append(a)
#print(number)
for a in number:
    res = requests.get(f'http://numbersapi.com/{a}/math?json')
    data = res.json()
    #print(data)
    if data['found'] == True:
        print('Interesting')
    else:
        print('Boring')


