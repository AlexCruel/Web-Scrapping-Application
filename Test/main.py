import requests
from bs4 import BeautifulSoup
import openpyxl

class Site():

    def __init__(self, HOST, URL):
        self.HOST = HOST
        self.URL = URL
        self.HEADERS = {
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'
        }

    def get_html(self):
        r = requests.get(self.URL, headers=self.HEADERS)
        return r

    def get_content(self, html, arg, select_class, find_str):
        soup = BeautifulSoup(html, 'html.parser')
        #items = soup.find_all(arg, class_=select_class)
        testItem = eval('soup.' + find_str)
        cards = []
        cards.append(
            {
                'price': testItem
            }
        )

        # for item in items:
        #     cards.append(
        #         {
        #             'price': item.find_str
        #         }
        #     )
        return cards

    def save_document(self, testItem, location):
        workbook = openpyxl.load_workbook('./1ak.by.xlsx')
        sheet = workbook.active

        for item in testItem:
            sheet[location] = item['price']

        workbook.save('./1ak.by.xlsx')

    def parser(self, arg, select_class, find_str, location):
        html = self.get_html()
        if html.status_code == 200:
            cards = []
            cards.extend(self.get_content(html.text, arg, select_class, find_str))
            self.save_document(cards, location)