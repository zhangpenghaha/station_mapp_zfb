import datetime

def get_当前年月():
    now_time=datetime.datetime.now().strftime('%Y-%m-')
    listtime=now_time.split("-")
    now_year_month=listtime[0]+"年"+listtime[1]+"月"
    return now_year_month

def get_当前年月日():
    """
    ex: 2001-01-01
    """
    return datetime.datetime.now().strftime('%Y-%m-%d')


def get_当前年月_个位去零():
    now_time=datetime.datetime.now().strftime('%Y-%m-')
    year=now_time.split("-")[0]
    mouth=int(now_time.split("-")[1])
    now_year_month=year+"年"+str(mouth)+"月"
    return now_year_month

def get_获取当前星期():
    today_number=datetime.datetime.now().weekday()
    datedict={0:"星期一",1:"星期二",2:"星期三",3:"星期四",4:"星期五",5:"星期六",6:"星期日"}
    today = datedict[today_number]
    return today

def get_指定日期星期(time):
    today_number=datetime.datetime.strptime(time,"%Y%m%d").weekday()
    datedict = {0: "星期一", 1: "星期二", 2: "星期三", 3: "星期四", 4: "星期五", 5: "星期六", 6: "星期日"}
    today=datedict[today_number]
    return today

def get_当前日期加指定日(day,format=True):
    if format==True:
        return (datetime.datetime.now()+datetime.timedelta(days=day)).strftime('%Y-%m-%d')
    elif format==False:
        return (datetime.datetime.now() + datetime.timedelta(days=day)).strftime('%Y%m%d')

def get_当前月日():
    now_time=datetime.datetime.now().strftime('%m-%d')
    listtime=now_time.split("-")
    now_month_day=listtime[0]+"月"+listtime[1]+"日"
    return now_month_day

# a=get_当前日期加指定日(60)
# b=get_指定日期星期("20190716")
# print(b)

if __name__ == '__main__':
   print(get_当前日期加指定日(1))