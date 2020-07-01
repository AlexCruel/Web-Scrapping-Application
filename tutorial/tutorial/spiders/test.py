import scrapy
import xlsxwriter

class Test(scrapy.Spider):
    name = 'test'

    workbook = xlsxwriter.Workbook('test.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.set_column('A:A', 20)

    bold = workbook.add_format({'bold': True})

    worksheet.write('A1', 'Hello, World!')
    worksheet.write('A2', 'It\'s me!!!!')
    worksheet.write('A3', 'Bold', bold)

    workbook.close()
