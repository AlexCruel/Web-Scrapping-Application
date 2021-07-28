import requests
from bs4 import BeautifulSoup
import csv

CSV = 'information.csv'
HOST = 'https://atl.ua/'
URL = 'https://atl.ua/akkumulyatory/bosch/primenyaemost-legkovye'
HEADERS = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='catalog-col-content top catalog-wrapper-column is-center')
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('div', class_='product-micro-title').find('a').get('href'),
                'price': item.find('div', class_='product-micro-price'),
                'link_product': item.find('div', class_='product-micro-title')
            }
        )
    return cards

def save_document(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Цена', 'Ссылка'])
        for item in items:
            writer.writerow([item['title'], item['price'], item['link_product']])

def parser():
    PAGENATION = input('Укажите количество страниц для парсинга: ')
    PAGENATION = int(PAGENATION.strip())

    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGENATION):
            print(f'Парсим страницу: {page}')
            html = get_html(URL, params={'page': page})
            cards.extend(get_content(html.text))
            save_document(cards, CSV)
    else:
        print('Error: site doesn\'t respond')

parser()