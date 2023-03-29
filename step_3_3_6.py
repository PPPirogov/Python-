import requests, re

A = input()
B = input()
Answer = 'No' # 'Yes'

C = B.replace('stepik.org','stepic.org')
B = C
D = A.replace('stepik.org','stepic.org')
A = D
site =requests.get(A).text

link = re.findall("href=[\"\'](ht.*?)[\"\']", site)
for a in link:
    if B in a:
        Answer = 'Yes'
        break
    else:
        site2 = requests.get(a).text
        link2 = (re.findall("href=[\"\'](ht.*?)[\"\']", site2))
        for b in link2:
            if B in b:
                Answer = 'Yes'
                break
print(Answer)