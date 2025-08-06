import requests

response = requests.get('http://books.toscrape.com/')

print(response.status_code)
print(response.ok)

if response.ok:
    print(response.text)
else:
    print('Server Error')