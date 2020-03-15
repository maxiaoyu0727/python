#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   2.py
@Time    :   2020/03/13 01:06:57
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#编写一个函数,接收n个数字，求这些参数数字的和
def sum(n):
    list1=[]
    for i in range(0,n):
        num=int(input("请输入数字："))
        list1.append(num)
    print(list1)
    sum=0
    for x in list1:
        sum=sum+x
    print(sum)
sum(5)
    