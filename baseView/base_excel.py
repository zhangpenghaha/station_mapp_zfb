import xlrd
import os


def read_excel(file_name,sheet_num):
    data_list = []
    # book = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\station_mapp\data\test_data.xlsx", file_name)
    book = xlrd.open_workbook(".%sdata%s%s" % (os.sep, os.sep, file_name))

    sheet1 = book.sheet_by_name(sheet_num)
    # 获取行数
    rows = sheet1.nrows
    # 获取列数
    coles =sheet1.ncols
    # 读取每一列的数据
    # for c in range(coles):
    #     c_values = sheet1.col_values(c)
    #     print(c_values)
    # 读取每一行的数据
    for r in range(rows):
        r_values = sheet1.row_values(r)
        data_list.append(r_values)
    # 读取指定单元格数据
    # print(sheet1.cell(1,1))
    print(data_list)
    return data_list

if __name__ == '__main__':
    read_excel("test_data.xlsx", "login")