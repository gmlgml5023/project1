import requests
from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/item/sise.nhn?code=005930'

res = requests.get(URL)
bs = BeautifulSoup(res.text, 'html.parser')

result = bs.select('td.num > span.tah.p11')


for data in result:
    print(data.text.strip())

