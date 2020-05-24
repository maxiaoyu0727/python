#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   exe0401.py
@Time    :   2020/04/27 23:42:57
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#定义一个高阶函数, 实现加,减,乘,除计算器功能;
'''
def plus(a,b):
    return (a+b)

def minus(a,b):
    return (a-b)

def multiply(a,b):
    return (a*b)

def divide(a,b):
    return (a/b)

def coculation(plus,minus,multiply,divide):
    list1=list(input('请输入想进行的运算(用空格隔开)：').split(' '))
    a=int(list1[0])
    b=int(list1[2])
    if list1[1]=='+':
        return(plus(a,b))
    elif list1[1]=='-':
        return(minus(a,b))
    elif list1[1]=='*':
        return(multiply(a,b))
    elif list1[1]=='/':
        return(divide(a,b))
print('结果为：',coculation(plus,minus,multiply,divide))

coculation(plus,minus,multiply,divide)
'''


#map()使用示例
'''
def square(x):    return x**2
list1=[1,3,5,7]
res=map(square,list1)
print(list(res))
'''

#reduce()用法示例
'''
from functools import reduce
def plus(x,y):
    return(x+y)
print(reduce(plus,[1,2,3,4,5]))  
'''

#filter()用法示例
'''
list1=[1,2,3,4,5,6,7,8,9,10]
def ifeven(x):
    return (x%2==0)
print(list(filter(ifeven,list1)))
'''


#利用闭包返回一个计数器函数，每次调用它返回递增整数：
'''
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
'''

#定义一个函数, 做2个数的加法;  然后我们定义一个装饰器, 对原函数记录运行日志
'''
def log(func):
    def wrapper(*args, **kw):
        print('加法被执行了')
        return func(*args, **kw)
    return wrapper

@log
def plus():
    list1=list(input('请输入想进行的运算(用空格隔开)：').split(' '))
    a=int(list1[0])
    b=int(list1[2])
    return (a+b)
print(plus())
'''