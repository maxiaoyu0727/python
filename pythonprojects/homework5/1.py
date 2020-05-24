#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   1.py
@Time    :   2020/04/27 23:36:39
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#编写一个装饰器，能计算其他函数的运行时间；

import time
def decorator(func):
    def run_time():
        starttime=time.time()
        func()
        endtime=time.time()
        print('运行时间为:',endtime-starttime)
    return run_time


@decorator
def printfunc():
    print('运行了一段程序')

printfunc()