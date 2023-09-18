import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

list_date = []
list_price = []

for i in range(2, 5, 1):
    
    URL = 'https://finance.naver.com/item/sise_day.naver?code=005930&'
    URL = URL+'page='+str(i)
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

    res = requests.get(URL, headers = headers)
    bs = BeautifulSoup(res.text, 'html.parser')

    result_date = bs.select('table.type2 tr > td > span.tah.p10.gray03')
    # print(result_date)
    result_price = bs.select('table.type2 tr > td.num > span.tah.p11')
    # print(result_price[0])


    for data1 in result_date:
        date = data1.text
        list_date.append(date)
    # print(list_date)
    
    for i in range(0, len(result_price), 6):
        price = result_price[i].text
        list_price.append(price)
    # print(list_price)

stock = pd.DataFrame({'Date' : list_date, 'Price' : list_price})
stock['Date'] = pd.to_datetime(stock.Date)
stock = stock[stock['Date'].dt.month == 8]

stock.to_csv('stock_info.csv', index = False)