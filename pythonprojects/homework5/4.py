#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   4.py
@Time    :   2020/05/12 20:15:32
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here

#编写装饰器来实现，对目标函数进行装饰，分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
#     三个目标函数分别为：
#     A 打印输出20000之内的素数；
#     B 计算整数2-10000之间的素数的个数；
#     C 计算整数2-M之间的素数的个数；
#  可以观看给的视频材料，仿照示例来做；

def decorator1(fun):
    def no_return_no_argument():
        print('目标函数无参数无返回值')
        fun()
    return no_return_no_argument

def decorator2(func):
    def no_argument():
        print('目标函数有返回值')
        res=func()
        return res
    return no_argument

def decorator3(func):
    def no_return(*args):
        print('目标函数有参数')
        func(*args)
    return no_return

'''
@decorator1
def prime_num1():
    for i in range(1,20001):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)
prime_num1()


@decorator2
def prime_num2():
    count=0
    for i in range(2,20001):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            count+=1
    return count
print(prime_num2())
'''

@decorator3
def prime_num3(m):
    count=0
    for i in range(2,m+1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            count+=1
    print(count)
prime_num3(50)
