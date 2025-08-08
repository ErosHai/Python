from bs4 import BeautifulSoup

import requests

# 请求获取到网页html
content = requests.get('https://books.toscrape.com/').text

# 解析html 并提取想要的内容
soup = BeautifulSoup(content,'html.parser')

# 通过类名找到对应书价格
allPrice = soup.find_all('p',attrs={'class': 'price_color'})

for price in allPrice:
    print(price.string[2:])

# 通过层层遍历找到对应书名
allTitle = soup.find_all('h3')
for title in allTitle:
     print(title.find('a').string)