#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   3.py
@Time    :   2020/03/12 11:21:06
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here

#定义2个列表，并初始化；  找出这2个列表中，相同的元素并输出；
list1=['maxiaoyu']
list2=['maxiaojia','maxiaoyu']
set1=set(list1)
set2=set(list2)
list3=list(set1&set2)
print(list3)