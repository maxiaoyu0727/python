#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   5.py
@Time    :   2020/03/15 16:33:30
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者

def change(dict1):
    i=1
    for x in dict1.values():
        print("字典中第",i,"个value的长度为",len(x))
        str1=x
        if len(x)>2:
            x=str1[0:2]
            dict1[i]=x
        i+=1
    
    print("修改后的字典为：",dict1)
    
dict1={1:'ma',2:'xiao',3:'yu',4:'shi',5:'hua',6:'bei',7:'dian'}
change(dict1)