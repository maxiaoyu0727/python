#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   7.py
@Time    :   2020/04/26 22:28:15
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#使用python代码统计一个文件夹中所有文件的总大小
import os

def totalsize(path):
    size=0
    dirlist=os.listdir(path)
    for file in dirlist:
        newpath=os.path.join(path,file)
        if(os.path.isfile(newpath)):
            filesize=os.path.getsize(newpath)
            size+=filesize
        else:
            totalsize(newpath)
    return size
print(totalsize('/Users/maxiaoyu/Desktop/python'))
