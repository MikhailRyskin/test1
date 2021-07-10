import requests
import json

my_req = requests.get('https://swapi.dev/api/people/1/')
# print(my_req.text)

my_dict = json.loads(my_req.text)
print(my_dict)
# my_dict['name'] = 'MMM2021'

with open('example.json', 'w') as file:
    json.dump(my_dict, file, indent=4)

url = my_dict['homeworld']
homeworld_req = requests.get(url)
homeworld = json.loads(homeworld_req.text)


print('дом для {n1} это {n2}'.format(n1=my_dict['name'], n2=homeworld['name']))
