#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   9.py
@Time    :   2020/03/15 17:51:01
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here

#定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序(冒泡排序,  也可以直接使用相关的函数)
def sort(list1):
    list1.sort(key=None, reverse=False)
    print(list1)
list1=list(input("请输入一组数字：").split(','))
sort(list1)