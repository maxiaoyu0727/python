#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   2.py
@Time    :   2020/05/26 17:59:40
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
 #给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；

import requests
import queue 
import os
import threading

def readfile():
    l=[]
    with open('/Users/maxiaoyu/Desktop/python/url_data.txt','r',encoding="gbk") as f:
        for i in f.readlines():
            l.append(i)
    return l
print(readfile())

def getHtmlText(url):
    try:        # 网络连接有风险，异常处理很重要
        r = requests.get(url,timeout=30)    # 查一下这个方法的使用
        r.raise_for_status()       # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "出现异常"
def main():
    for i in readfile():
        print(getHtmlText(i))
main()
