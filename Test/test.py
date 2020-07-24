import openpyxl

workbook = openpyxl.load_workbook('./hello.xlsx')

def write(workbook):
    sheet = workbook.active
    sheet['A4'] = 'Male'
    sheet['B3'] = 'Some text'
    sheet['B4'] = 'Another one'
    workbook.save('hello.xlsx')

write(workbook)