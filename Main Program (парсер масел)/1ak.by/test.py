from bs4 import BeautifulSoup
import requests
import locale

locale.setlocale(locale.LC_ALL, "de")  

def parse():
    URL = 'https://1ak.by/shop/masla/motornye-masla/dlya-legkovyh-avtomobilej/gazpromneft-super-5w-40.html'
    HEADERS = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'
    }

    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    item = soup.find('input', type='hidden', class_='js-ch-product-price gec-product-price')

    print(item['value'])

parse()