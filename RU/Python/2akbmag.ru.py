import requests
from bs4 import BeautifulSoup
import csv

CSV = 'akbmag.ТюменьAuto.csv'
HOST = 'https://akbmag.ru/'
URL = 'https://spb.akbmag.ru/catalog/avtomobilnye_akkumulyatory_alphaline/'
HEADERS = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='product-tile')
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('h2', class_='product-tile-title').get_text(strip=True),
                'price': item.find('div', class_='product-price').get_text(strip=True),
                'price2': item.find('strong', class_='product-price-current').get_text(strip=True),
                'characteristic': item.find('div', class_='tech-list-block').get_text(strip=True),
                'link_product': HOST + item.find('h2', class_='product-tile-title').find('a').get('href')
            }
        )
    return cards

def save_document(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Цена', 'При обмене', 'Характеристика', 'Ссылка'])
        for item in items:
            writer.writerow([item['title'], item['price'], item['price2'], item['characteristic'], item['link_product']])

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        cards.extend(get_content(html.text))
        save_document(cards, CSV)
    else:
        print('Error: site doesn\'t respond')

parser()