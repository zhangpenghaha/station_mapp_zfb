from function.funcdate import *


def tools_选择日期(day=60):
    days=get_当前日期加指定日(day)
    listdate=days.split("-")
    if int(listdate[2])<10:
        return listdate[2][1]
    else:
        return listdate[2]
def test():
    return "a","b"

if __name__ == '__main__':
    print("".join(tuple(test())))


