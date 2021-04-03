import re
import requests
import json
from bs4 import BeautifulSoup


userName = 'JasonCZH'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
url = 'https://codeforces.com/api/user.rating?handle='+userName
response = requests.get(url,headers = headers )
home_page = response.json()
r = response.text.encode()
print(r)
print(home_page)
result = home_page['result']
for i in result:
    #json.dump(i, open("rank_data", "w"))
    print(i['contestName'], i['oldRating'], i['newRating'])


'''
rank = open("C:\\Users\\ASUS\\PycharmProjects\\pythonProject1\\rank_data.json", "r")
ls = json.load(rank)
data = [list(ls[0].keys())]
for item in ls:
    data.append(list(item.values()))
rank.close()
fw = open("C:\\Users\\ASUS\\PycharmProjects\\pythonProject1\\rank_data.csv", "w")
for line in data:
    fw.write(",".join(line) + "\n")
fw.close()

soup = BeautifulSoup(home_page, 'lxml')
script = soup.find(id='getListByCountryTypeService2true')
text = script.string
# print(text)

# json_str = re.findall(r'\[.+\]', home_page)[0]
# print(json_str['oldRating'])
# print(json_str)

last_day_situation = json.loads(json_str)
# print(last_day_situation)

with open("data/last_day_situation.json", 'w', encoding='utf8') as fp:
    json.dump(last_day_situation, fp, ensure_ascii=False)
'''
