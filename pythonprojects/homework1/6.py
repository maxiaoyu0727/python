#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   6.py
@Time    :   2020/03/12 12:10:15
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here

# 前面2个元素为0，1，输出100以内的斐波那契数列
i=0
j=1
list1=[0,1]
fib=0
while (fib<100):
    fib=list1[i]+list1[j]
    i+=1
    j+=1
    if(fib<100):
        list1.append(fib)
print(list1)
