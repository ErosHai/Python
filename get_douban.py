from bs4 import BeautifulSoup

import requests

headers = {
    'user-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
}

response = requests.get('https://movie.douban.com/top250',headers=headers).text

soup = BeautifulSoup(response,'html-parser')

print(soup)