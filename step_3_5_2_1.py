import requests
city = input("City? ")
api_url = 'http://api.openweathermap.org/data/2.5/weather'

params = {
    'q': city,
    'appid': '56022fa7c6f904d732a351c39637250f',
    'units':'metric'
}

res = requests.get(api_url, params=params)
# print(res.status_code)
# print(res.headers["Content-Type"])
#print(res.json)
data = res.json()
print(data)

template = 'Curent temperature in {} is {} '
print(template.format(city, data['main']))
print(template.format(city, data['main']['temp']))
