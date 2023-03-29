import requests

# #res = requests.get("https://docs.python.org/3.5/")
# res = requests.get("https://docs.python.org/3.5/_static/py.png")
# print(res.status_code)
# print(res.headers['Content-Type'])
#
# print(res.content)
# print(" ")
#
# with open("python.png","wb") as f:
#     f.write(res.content)
#print(res.text)

pes = requests.get("https://yandex.ru/search/",
                   params={"text": "Stepic"
                           ,"test":"test1"
                           ,"name":"Name With Spaces"
                           ,"list":["test1","test2"]
                           })
print(pes.status_code)
print(pes.headers['Content-Type'])
print(pes.url)
print(pes.text)