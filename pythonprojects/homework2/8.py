#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   8.py
@Time    :   2020/03/15 17:29:27
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，
#并打印出该字符及其出现的次数。
#例如，输入 aaaabbc，输出：a:4
def maxchar(str1):
    list1=list(str1)
    dict1={}
    length=len(list1)
    i=0
    while(i<length):
        str1=list1[i]
        if(str1 not in dict1.keys()):
            dict1[str1]=1
        elif(str1 in dict1.keys()):
            dict1[str1]+=1
        i+=1
    keylist=list(dict1.keys())
    valuelist=list(dict1.values())
    flag1=keylist[0]
    flag2=valuelist[0]
    for x in dict1.keys():
        if dict1[x]>flag2:
            flag2=dict1[x]
            flag1=x
    print(flag1,':',dict1[flag1])
str1=input('请输入字符串：')
maxchar(str1)