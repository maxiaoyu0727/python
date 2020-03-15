#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   6.py
@Time    :   2020/03/15 17:00:38
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#定义一个函数, 打印输出n以内的斐波那契数列
def fib(n):
    i=0
    #flag=0
    j=1
    list1=[0,1]
    fib=0
    while (fib<n):
        fib=list1[i]+list1[j]
        i+=1
        j+=1
        if(fib<n):
            list1.append(fib)
       # flag+=1
    print(list1)
fib(100)