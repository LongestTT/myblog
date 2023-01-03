import time
import datetime


# 计算两个日期相差天数，自定义函数名，和两个日期的变量名。
def Caltime():
    # 生成当前日期, 样式为: 2022-07-15
    date1 = '2022-12-25'
    today_time = datetime.datetime.now().strftime("%Y-%m-%d")

    date1 = time.strptime(date1, "%Y-%m-%d")
    date2 = time.strptime(today_time, "%Y-%m-%d")
    date1 = datetime.datetime(date1[0], date1[1], date1[2])
    date2 = datetime.datetime(date2[0], date2[1], date2[2])
    return (date2 - date1).days
