from bs4 import BeautifulSoup

import requests

# 请求获取到网页html
content = requests.get('https://books.toscrape.com/').text

# 美化html 并提取想要的内容
soup = BeautifulSoup(content,'html.parser')

allPrice = soup.find_all('p',attrs={'class': 'price_color'})

for price in allPrice:
    print(price.string[2:])
