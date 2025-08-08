from bs4 import BeautifulSoup

import requests

headers = {
    'user-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
}

top_num = 0

for start_num in range(0,250,25):
    response = requests.get(f'https://movie.douban.com/top250?start={start_num}',headers=headers).text

    soup = BeautifulSoup(response,'html.parser')

    all_title = soup.find_all('span',attrs={'class':'title'})

    for title in all_title:
        chinese_title = title.string
        if '/' not in chinese_title:
            top_num += 1
            print(f'Top {top_num} -《{chinese_title}》' )