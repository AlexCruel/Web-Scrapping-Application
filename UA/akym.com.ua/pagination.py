import requests
from bs4 import BeautifulSoup
import csv

CSV = 'information.csv'
HOST = 'https://akym.com.ua/'
URL = 'https://akym.com.ua/category/645_akkumuljatory-varta/'
HEADERS = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('ul', class_='product_table product-list')
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('li').find('span', class_='product_param').get_text(strip=True),
                # 'amperage': item.find('ul', class_='product-view-info__list').find_all('li')[3].find('span').get_text(strip=True),
                # 'capacity': item.find('ul', class_='product-view-info__list').find_all('li')[2].find('span').get_text(strip=True),
                # 'price': item.find('div', class_='product-view-prices__base-price-number').get_text(strip=True),
                # 'link_product': HOST + item.find('div', class_='product-view-title').find('a').get('href')
            }
        )
    return cards

def save_document(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Ток', 'Емкость', 'Цена', 'Ссылка'])
        for item in items:
            writer.writerow([item['title']])

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