#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   7.py
@Time    :   2020/03/15 17:05:19
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here

import random
#随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;  
#    A---成绩>=90;  
#    B-->成绩在 [80,90)
#    C-->成绩在 [70,80)
#    D-->成绩<70
def level():
    alist=[]
    blist=[]
    clist=[]
    dlist=[]
    list1=[]
    for i in range(0,20):
        list1.append(random.randint(30,101))
    for x in list1:
        if x>=90:
            alist.append(x)
        elif x<90 and x>=80:
            blist.append(x)
        elif x<80 and x>=70:
            clist.append(x)
        else:
            dlist.append(x)
    print('成绩列表为：')
    print(list1)
    print('等级为A的成绩列表为：')
    print(alist)
    print('等级为B的成绩列表为：')
    print(blist)
    print('等级为C的成绩列表为：')
    print(clist)
    print('等级为D的成绩列表为：')
    print(dlist)
level()