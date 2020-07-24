import scrapy
import xlsxwriter
from scrapy.exporters import XmlItemExporter

class Test(scrapy.Spider):
    name = 'test'

    start_urls = ['http://quotes.toscrape.com/']

    workbook = xlsxwriter.Workbook('test.xlsx')
    worksheet = workbook.add_worksheet()

    def parse(self, response, worksheet, name_author):
        author_page_links = response.css('.author + a')

        worksheet.write('A1', name_author)

        return response.follow_all(author_page_links, self.parse_author)

    def parse_author(self, response, worksheet):
        name_author = response.css('.author-title::text')

        return name_author

    workbook.close()
