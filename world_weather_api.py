

import requests
from influxdb import InfluxDBClient


# api-key
appid = '42440f4477df938ae11483f074a8cdfd'
city_name = input('Enter name of the City: ')

# get the respose from url
response = requests.get(
    f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={appid}')


# print resposne
print(response)

json_body = response.json()

client = InfluxDBClient('172.17.0.2', 8086, 'root', 'root', 'example')
client.create_database('example')
client.write_points(json_body)
result = client.query('select value from cpu_load_short;')
