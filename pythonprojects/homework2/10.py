#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   10.py
@Time    :   2020/03/15 18:08:21
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)
def cacluate():
    list1=list(input('请输入想进行的运算(用空格隔开)：').split(' '))
    num1=int(list1[0])
    num2=int(list1[2])
    if list1[1]=='+':
        num3=num1 + num2
    elif list1[1]=='-':
        num3=num1 - num2
    elif list1[1]=='*':
        num3=num1 * num2
    elif list1[1]=='/':
        num3=num1 / num2
    print('结果为：',num3)
cacluate()
