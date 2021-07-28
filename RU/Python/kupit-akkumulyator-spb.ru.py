import requests
from bs4 import BeautifulSoup
import csv

CSV = 'test.csv'
HOST = 'https://kupit-akkumulyator-spb.ru/'
URL = 'https://kupit-akkumulyator-spb.ru/kategorii/akkumulyatory_dlya_legkovyh_avto/?order_filter_placeholder=1&order_filter_name=0&catalog_layout=1&catalog_per_page=48&fields_filter%5Bcustom_field_1481402382%5D=294733'
HEADERS = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tr', class_='cat-item-active')
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('td', class_='content_column').find('a').get_text(strip=True),
                'price': item.find('div', class_='price old_price').get_text(strip=True),
                'price2': item.find('div', class_='price').get_text(strip=True),
                'characteristic': item.find('div', class_='obj_short_desc').get_text(strip=True),
                'link_product': HOST + item.find('a', class_='title_left').get('href')
            }
        )
    return cards

def save_document(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Цена', 'При сдаче', 'Характеристика', 'Ссылка'])
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