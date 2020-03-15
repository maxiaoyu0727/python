#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   5.py
@Time    :   2020/03/12 11:33:45
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here

import random
#使用random模块，生成随机数，来初始化一个列表，元组；使用了 random 模块的 randint() 函数来生成随机数，查询一下相关函数的用法；

list1=[]
tuple1=tuple()
len1=input("请输入列表和元组的长度：")
len=int(len1)
i=0
while(i<=len):
    x=random.randint(0,11)
    list1.append(x)
    tuple1=tuple1+(x,)
    i+=1
print(list1)
print(tuple1)