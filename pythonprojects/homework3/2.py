#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   2.py
@Time    :   2020/04/10 01:25:52
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
#第一行： xxxx
#第二行： xxxx
L=[]
with open('/Users/maxiaoyu/Desktop/python/pythonprojects/input.txt','r') as f:
    i=1
    for line in f:
        L.append(line)
    for x in L:
        print('第',i,'行:',x) 
        i+=1
