#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   3.py
@Time    :   2020/03/15 00:27:53
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
import random

#编写一个函数, 传入一个数字列表, 输出列表中的奇数;
#数字列表请用随机数函数生成;
def odd(list1):
    list2=[]
    print("列表中的奇数有：")
    for x in list1:
        if (x%2!=0):
            list2.append(x)
    print(list2) 
i=0
list1=[]
while(i<=10):
    x=random.randint(0,11)
    list1.append(x)
    i+=1
print("原列表为：",list1)
odd(list1)