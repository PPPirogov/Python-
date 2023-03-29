# import requests, re
#
# #A = input()
# #B = input()
# Answer = 'No' # 'Yes'
# A = "https://stepik.org/media/attachments/lesson/24472/sample1.html"
# B = "https://stepik.org/media/attachments/lesson/24472/sample2.html"
# #B.replace('stepik.org','stepic.org')
# site =requests.get(A).text
# #print(site)
# link = re.findall("href=[\"\'](ht.*?)[\"\']", site)
# C = B.replace('stepik.org','stepic.org')
# B = C
# #print(C)
# #print(B)
# for a in link:
#     # a.replace('stepic.org','stepik.org')
#     # print(a)
#     if B in a:
#         Answer = 'Yes'
#         break
#     else:
#         site2 = requests.get(a).text
#         link2 = (re.findall("href=[\"\'](ht.*?)[\"\']", site2))
#         #print(link2)
#         for b in link2:
#             # b.replace('stepic.org', 'stepik.org')
#             # print(b)
#             if B in b:
#                 Answer = 'Yes'
#                 break
# print(Answer)

import time
print(strptime("11/20/2002 03:20:00 PM", "%Y"))