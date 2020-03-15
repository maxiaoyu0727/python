#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   7.py
@Time    :   2020/03/12 12:27:38
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#打印输出9*9乘法表，按照下面的格式
x=1
while(x in range(1,10)):
    y=1
    while(y in range(1,x+1)):
        print(x,'*',y,'=',x*y,' ',end='')
        y+=1
    x+=1
    print('\n')