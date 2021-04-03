# Author:JasonCZH4
# Date:2021/3/28 17:29
import re
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import tesserocr

'''
search = '远坂凛'
url = 'https://sso.scnu.edu.cn/AccountService/static/login/images/bg_login.png'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 '
                  'Safari/537.36 QIHU 360SE', 'Connection': 'keep-alive',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
try:
    response = requests.get(url, headers=headers)
    # 必须加UA头，不然会返回一个登录页面
    print(response.raise_for_status())
    # 查看状态信息，返回的是200，说明返回信息正确并且已经获得该链接相应内容。
    print(response.encoding)
    # 查看编码格式，这个格式是jbk，说明我们从http的头部分已经可以解析出网站信息。
    r = response.text
    print(r)
except:
    print("爬取失败")

# print(r)

'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 '
                  'Safari/537.36 QIHU 360SE', 'Connection': 'keep-alive',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
result = requests.get('https://sso.scnu.edu.cn/AccountService/user/rancode.jpg?m=1.0024973463803444', headers=headers)
try:
        image = Image.open(BytesIO(result.content))
        print(image)
        name = 'scnu_1' + '.jpg'
        image.save(r'E:\\python_img_text\\' + name)
        print('成功爬取！')
except:
        print('下载失败！')
'''
cnt = 0
soup = BeautifulSoup(r, 'lxml')
link = soup.find_all('a', attrs={'class': 'iusc'})
link_all = link[0:]  # 将link变成list类型
print(link)
print(link_all)
print(type(link))
print(type(link_all))
for i in link_all:
    temp = link_all[cnt:cnt + 1]
    img_url = str(temp)
    print(type(img_url))
    print(img_url)
    cnt += 1
    final_url1 = re.findall(r'murl\":\".+[j][p][g]\"', img_url)
    if final_url1:
        final_url2 = re.findall(r'http.+[j][p][g]', final_url1[0])
        print(final_url1[0])
        print(final_url2[0])
        result = requests.get(final_url2[0], headers=headers)
        result.encoding = result.apparent_encoding

    try:
        image = Image.open(BytesIO(result.content))
        name = str(cnt) + '.jpg'
        image.save(r'E:\\python_img_text\\' + name)
        print('成功爬取！')
    except:
        print('下载失败！')
'''
