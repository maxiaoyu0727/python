#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   2.py
@Time    :   2020/03/12 01:19:39
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#一个字典中，存放了10个学生的学号（key）和分数（value）；请筛选输出，大于80分的同学（按照格式：学号：分数）
dict1={101:68,102:79,103:98,104:87,105:38,106:93,107:89,108:60,109:100,110:40}
for k in dict1.keys():
    if(dict1[k]>80):
        print(k,':',dict1[k])