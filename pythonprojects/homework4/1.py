#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   1.py
@Time    :   2020/04/21 23:57:11
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；
#用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
#提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)

import time
import datetime
from collections import deque

def insert1():
    list1=[0,1,2,3,4,5,6,7,8,9]
    list1.insert(0,98)
    list1.append(99)
    print(list1)

def insert2():
    list2=[0,1,2,3,4,5,6,7,8,9]
    q=deque(list2)
    q.append(99)
    q.appendleft(98)
    list3=list(q)
    print(list3)


def time_difference(time1,time2):
    print(time2-time1)


start = time.time()
insert1()
end = time.time()
time1=end-start

start1=time.time()
insert2()
end1=time.time()
time2=end1-start1

time_difference(time1,time2)