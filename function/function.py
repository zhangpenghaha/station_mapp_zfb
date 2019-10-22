# coding:utf8
import os
import xlrd
from xlutils.copy import copy
"""    
    文件路径拼接方法：
    返回API_Auto_Project文件的绝对路径
    提高脚本的可移植性
"""
def path_项目路径():

    " 获取当前文件绝对路径 "
    ex_当前文件绝对路径 = os.path.abspath(__file__)

    " 获取项目路径，如果项目文件修改这里需要及时修改 "
    ex_项目路径 = ex_当前文件绝对路径.split("station_mapp_zfb")[0]+ 'station_mapp_zfb\\'
    return ex_项目路径

    """
    从EXCEL中读取测试数据
    如果想获取整数类型记得加int()函数
    """

def excel_read(测试数据相对路径,测试数据所在的sheet名字):
    with xlrd.open_workbook(path_项目路径()+测试数据相对路径) as file:
        "通过sheet名定位,测试用例位置"
        sheet_数据 = file.sheet_by_name(测试数据所在的sheet名字)
        "获取sheet中的行数，测例个数"
        num_行数 = sheet_数据.nrows
        "获取sheet中的列数，参数个数"
        num_列数 = sheet_数据.ncols
        "定义一个空总列表，用于存放每一行的测例数据，在test_case模块中ddt使用"
        list_测试数据 = []
        "遍历所有行，忽略首行"
        for h in range(1,num_行数):
            dict_每行数据 = {}
            for l in range(num_列数):
                dict_每行数据[sheet_数据.cell(0,l).value] = sheet_数据.cell(h,l).value
            list_测试数据.append(dict_每行数据)
        return list_测试数据

def search_sheet_index(test_data_file_path,sheet_name):

     with xlrd.open_workbook(path_项目路径()+test_data_file_path) as file:
         sheet_names_list = file.sheet_names()
         sheets_index = sheet_names_list.index(sheet_name)
         return sheets_index

def write_result_data(test_data_file_path,sheet_name,rows_number,status_actual=None,head_actual=None,body_actual=None):

    with xlrd.open_workbook(path_项目路径()+test_data_file_path) as oldWb:
        sheet_names_list = oldWb.sheet_names()
        sheet_index = sheet_names_list.index(sheet_name)
        newWb = copy(oldWb)
        newWs = newWb.get_sheet(sheet_index)
        "写入响应状态码实际结果！"
        newWs.write(rows_number, 13, status_actual)
        "写入响应头实际结果！"
        newWs.write(rows_number, 12, head_actual)
        "写入响应体实际结果！"
        newWs.write(rows_number, 14, body_actual)
        # wb.add_sheet(test_case_sheet_name, cell_overwrite_ok=True)
    newWb.save(path_项目路径()+test_data_file_path)

def get_flag():
    with open(path_项目路径()+r"config\flag.text","r") as f:
        data =f.read()
    return int(data)

def update_flag(flag):
    with open(path_项目路径()+r"config\flag.text","w") as f:
        f.write(str(flag))

if __name__ == '__main__':
    a=path_项目路径()
    # a=excel_read(r'testData\密码为空测试数据.xls',r"手机号密码测试数据")
    update_flag(1)
    b=get_flag()
    print(b)
