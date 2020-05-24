#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   exe1.12.py
@Time    :   2020/03/12 16:48:49
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here

#定义一个函数,来计算苹果的价格(重量*价格); 通过键盘输入重量和价格,然后调用函数来计算
'''
def total(weight,price):
    total=weight * price
    print('总价为：',total)

weight1=int(input('请输入苹果的重量：'))
price1=int(input("请输入苹果的价格:"))
total(weight1,price1)
'''

#定义一个函数,打印输出列表里面的元素;然后增加列表中的元素,然后再输出新的列表;
#主程序中,打印这个列表的地址(传参之前,传参之后)
'''
def printlist(list1,list2):
    print('旧列表为：',list1)
    list1.append(list2)
    print('新列表为：',list1)
list1=list(range(0,11))
list2=list(range(10,16))
print('传参前的地址：',id(list1))
printlist(list1,list2)
print('传参后的地址：',id(list1))    
'''

#初始化一个列表(1-20之间的整数) ; 然后 使用匿名函数,列表解析式, 来打印输出一个列表中的奇数;
'''
list1=list(range(1,21))
odd = filter(lambda x: x%2!=0, list1) #返回偶数
print(list(odd))
'''

#使用不定长参数定义一个函数;实现对输入数据的封装(封装成一个列表和字典),然后打印输出;
'''
def myfun(x,*args):
    print('第一个参数:', x)
    print('第二个参数:', args)
    for i in args:
        print('第二个参数里面的值:',i)
myfun(11,22,33,44,55)
myfun(11,'a','b','c',55)
'''

#试试这段代码
'''
from random import randint
data1=[randint(-10,10) for _ in range(10)]
print(data1)
'''