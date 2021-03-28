import xlrd
import os

#絶対パスを取得
book = xlrd.open_workbook(os.path.abspath('test_book.xlsx'))
print('--------------------------------')
print(book.nsheets)

print('--------------------------------')
for name in book.sheet_names():
    print(name)
