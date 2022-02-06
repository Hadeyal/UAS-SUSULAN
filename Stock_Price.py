import requests
from bs4 import BeautifulSoup

def priceTracker():


    url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    #print(soup)
    price = soup.find_all('div', {'class' : 'My(6px) Pos(r) smartphone_Mt(6px) W(100%) '})[0].find().text
    return price

print('Current Price : ' + priceTracker())

