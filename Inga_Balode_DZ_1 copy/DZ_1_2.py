import requests
import json
from pprint import pprint

end_point = "https://api.vindecoder.eu/3.1"
api_key = '53868031779e'
secret_key = '4c89f10f80'
id = 'decode'
vin = input("Введите VIN код автомобиля: ")
# например 'WBA7B01000G945106'

url = f"{end_point}/{api_key}/{secret_key}/{id}/{vin}.json"

req = requests.get(url)
data = json.loads(req.text)
print(data)

print(f'VIN номер: {data["decode"][0]["value"]}')
print(f'Марка автомобиля: {data["decode"][1]["value"]}')
print(f'Производитель: {data["decode"][2]["value"]}')
print(f'Страна: {data["decode"][3]["value"]}')
print(f'Тип: {data["decode"][4]["value"]}')
print(f'Модель: {data["decode"][8]["value"]}')
print(f'Год: {data["decode"][9]["value"]}')
print(f'Вы можете выполнить проверку еще для {data["balance"]["API Decode"]} VIN номеров')

