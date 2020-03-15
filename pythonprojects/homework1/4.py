#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   4.py
@Time    :   2020/03/12 11:26:19
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here

#判断用户输入的年份是否为闰年
year=int(input("请输入您想判断的年份："))
if (year%100!=0):
    if (year%4==0):
        print(year,"是闰年")
    else:
        print(year,"不是闰年")
elif(year%100==0):
    if(year%400==0):
        print(year,"是闰年")
else:
    print(year,"不是闰年")