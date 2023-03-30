import requests
import json
artists =[]
art = {}
with open('artists.txt','r') as te:
    for a in te:
        a=a.rstrip()
        artists.append(a)

client_id = '8a901aa2b17d346da5b1'
client_secret = '410e98eafaa9d97c349a192ef635c822'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]
#print(token)

headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers)

# разбираем ответ сервера
j = json.loads(r.text)
# for a in j:
#     print(a,j[a])
for a in artists:
    res = requests.get(f"https://api.artsy.net/api/artists/{a}", headers=headers)
    res.encoding = 'utf-8'
    data = res.json()
    art[data['sortable_name']] = data['birthday']
#print(art)
sorted_rooms = sorted(art.items(), key=lambda x: (x[1], x[0]))
for a in sorted_rooms:
    print(a)
# for a in art:
#     print(a,art[a])