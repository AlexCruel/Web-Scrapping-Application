import requests
from bs4 import BeautifulSoup
import openpyxl

HOST = 'https://1ak.by/'
URL = 'https://1ak.by/mag/brands/zubr/'
HEADERS = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='product')
    cards = []
    
    for item in items:
        cards.append(
            {
                'title': item.find('div', class_='product__title').get_text(strip=True),
                'price': item.find('div', class_='product__price').find('span').get_text(strip=True)
            }
        )
    return cards

def save_document(items):
    workbook = openpyxl.load_workbook('./1ak.by.xlsx')
    sheet = workbook.active

    for item in items:
        sheet['A2'] = item['title']
        sheet['B2'] = item['price']

    workbook.save('./1ak.by.xlsx')

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        cards.extend(get_content(html.text))
        save_document(cards)
    else:
        print('Error: site doesn\'t respond')

parser()