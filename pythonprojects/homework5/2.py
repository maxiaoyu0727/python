#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   2.py
@Time    :   2020/05/12 17:24:22
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中

import os
def decorator(func):
    def diary_write():
        sentence='你调用了一个函数'
        f=open('/Users/maxiaoyu/Desktop/python/pythonprojects/diary.txt','w')
        f.write(sentence)
        f.close()
        print(sentence)
        return func()
    return diary_write


@decorator
def printwords():
    print('我是一个函数')

printwords()