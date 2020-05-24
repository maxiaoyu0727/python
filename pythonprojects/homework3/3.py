#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   3.py
@Time    :   2020/04/10 01:35:58
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数); 然后按照分数从高到低进行排序输出
import os
L=[]
f=open('/Users/maxiaoyu/Desktop/python/pythonprojects/studentlist.txt','r')
for line in f:
    L.append(line.split())  #先把每一行设成一个学生的列表，再把学生列表加到总列表中
print(L,'\n')
L.sort(key=lambda X:X[2], reverse=True)
for stu in L:    
    print(stu,'\n')
f.close()
    
