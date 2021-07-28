import requests
from bs4 import BeautifulSoup
import csv

CSV = 'akb.AFA.csv'
HOST = 'https://akb.ru/'
URL = 'https://spb.akb.ru/catalog/search/?search=&filter-36%5B0%5D=81&filter-36%5B1%5D=128&filter-36%5B2%5D=10&filter-36%5B3%5D=92&filter-10%5Bmin%5D=1900&filter-10%5Bmax%5D=23600&filter-2%5Bmin%5D=12&filter-2%5Bmax%5D=240&filter-3%5Bmin%5D=0&filter-3%5Bmax%5D=1500&category_id%5B0%5D=1&enable_delivery=true&page=2'
HEADERS = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='slide')
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('a', class_='product-title').get_text(strip=True),
                'price': item.find('div', class_='last-cost').get_text(strip=True),
                'price2': item.find('div', class_='new-cost').get_text(strip=True),
                'characteristic': item.find('table', class_='info').get_text(strip=True),
                'link_product': HOST + item.find('a', class_='product-title').get('href')
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