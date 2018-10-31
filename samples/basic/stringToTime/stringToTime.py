# -*- coding: utf-8 -*-
import time, datetime, calendar
'''
python使用时间元组来表示，即struct_time。
time.time()返回当前的时间戳
time.localtime(time.time()) 参数是时间戳，返回struct_time对象
'''
# date to str
t = time.strftime("%Y-%m-%d %X", time.localtime())
print(t)
#str to date
d = time.strptime("2018-3-29", "%Y-%m-%d")
year, month, day = d[0:3]
date = datetime.datetime(year, month, day)
print(date)

# 返回日历
cal = calendar.month(2018, 3)
print(cal)
