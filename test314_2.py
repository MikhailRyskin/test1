import requests
import json

my_req = requests.get('https://swapi.dev/api/films/1/')
# print(my_req.text)

my_dict = json.loads(my_req.text)
print(my_dict['opening_crawl'])
