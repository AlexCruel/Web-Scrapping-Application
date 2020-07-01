import xlsxwriter

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A', 20)

bold = workbook.add_format({'bold': True})

worksheet.write('A1', 'Hello, World!')
worksheet.write('A2', 'It\'s me!!!!')
worksheet.write('A3', 'Bold', bold)

worksheet.write(3, 0, 123)
worksheet.write(4, 0, 123.456)
worksheet.write(5, 0, 123.456)

worksheet.write(4, 2, 123.456)

worksheet.write('B1', 'Title')
my_list = [1, 2, 3, 4, 5]

for row_num, data in enumerate(my_list):
    worksheet.write(row_num + 1, 1, data)

workbook.close()