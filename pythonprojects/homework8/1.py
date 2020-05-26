#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   1.py
@Time    :   2020/05/26 17:30:37
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here

#有100个同学的分数：数据请用随机函数生成；
#  A 利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
#  B 利用线程池来实现；

#多线程
'''
from time import sleep
import random
import threading

def A():
    for i in range(1,21):
        x=random.randint(50,100)
        print('学生{}的成绩为：{}'.format(i,x))
        sleep(1)
def B():
    for i in range(21,41):
        x=random.randint(50,100)
        print('学生{}的成绩为：{}'.format(i,x))
        sleep(1)
def C():
    for i in range(41,61):
        x=random.randint(50,100)
        print('学生{}的成绩为：{}'.format(i,x))
        sleep(1)
def D():
    for i in range(61,81):
        x=random.randint(50,100)
        print('学生{}的成绩为：{}'.format(i,x))
        sleep(1)
def E():
    for i in range(81,101):
        x=random.randint(50,100)
        print('学生{}的成绩为：{}'.format(i,x))
        sleep(1)

if __name__ == '__main__':
    thread1=threading.Thread(target=A)
    thread2=threading.Thread(target=B)
    thread3=threading.Thread(target=C)
    thread4=threading.Thread(target=D)
    thread5=threading.Thread(target=E)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
'''

#线程池
from multiprocessing import Pool
import random
from time import sleep

def A(m,n):
    for i in range(m,n):
        x=random.randint(50,100)
        print('学生{}的成绩为：{}'.format(i,x))
        sleep(1)

if __name__ == '__main__':
    po = Pool(5) 
    # Pool().apply_async(要调用的目标,(传递给目标的参数元祖,))
    # 每次循环将会用空闲出来的子进程去调用目标
    po.apply_async(A,(1,21))
    po.apply_async(A,(21,41))
    po.apply_async(A,(41,61))
    po.apply_async(A,(61,81))
    po.apply_async(A,(81,101))
    po.close()  # 关闭进程池，关闭后po不再接收新的请求
    po.join()  # 等待po中所有子进程执行完成，必须放在close语句之后
