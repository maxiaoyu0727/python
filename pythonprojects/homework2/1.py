#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   1.py
@Time    :   2020/03/13 01:02:29
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#第二次作业
#写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者
def length(target):
    length=len(target)
    return length
    
target=input("请输入对象(用逗号隔开):").split(',')
print(length(target))
