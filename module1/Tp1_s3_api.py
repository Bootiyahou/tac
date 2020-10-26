import json
import sys

import requests

def print_article (keyword):
    osm ="http://newsapi.org/v2/top-headlines?country=be&apiKey=f81764364b4848b4972eb8a87aae1f36"
    data = {'q': keyword, 'format': 'json'}
    resp = requests.get(osm, data)
    json_list = json.loads(resp.text)
    json_list
    for item in json_list ['articles']:
        print ( item ['title'] ,item['url'])

print_article ('di rupo')