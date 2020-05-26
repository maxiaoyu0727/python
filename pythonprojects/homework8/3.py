#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   3.py
@Time    :   2020/05/26 19:16:52
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#计算1～100000之间所有素数的个数， 要求如下:
#编写函数判断一个数字是否为素数，然后统计素数的个数；
#对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
#对比2：对比开启4个多进程和开启10个多进程两种方法的速度。

from multiprocessing import Pool
import threading
import time
def is_prime(i):
    if i==1 or i==2:
        return True
    elif(i!=1 and i!=2):
        for j in range(2,i):
            if i%j==0:
                return False
                break
        return True

def no_multi():
    time1=time.time()
    num=0
    for i in range(1,10000):
        if(is_prime(i)):
            num+=1
    time2=time.time()
    time3=time2-time1
    print('素数共有{}个'.format(num))
    print('不使用多进程所耗时间为',time3)

def multi(n):
    time1=time.time()
    po = Pool(n) 
    num=0
    # Pool().apply_async(要调用的目标,(传递给目标的参数元祖,))
    # 每次循环将会用空闲出来的子进程去调用目标
    for i in range(1,10000):
        flag=po.apply_async(is_prime,(i,))
        if(flag.get()):
            num+=1
    time2=time.time()
    time3=time2-time1
    print('素数共有{}个'.format(num))
    print('使用{}个多线程所耗时间为：{}'.format(n,time3))

def main():
    no_multi()
    multi(4)
    multi(10)
main()