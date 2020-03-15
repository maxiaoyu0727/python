#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   10.py
@Time    :   2020/03/12 15:34:48
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here

#给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出：
#提示：可以用字典来统计：key 是单词，value 是单词出现次数
#先创建一个字典，然后遍历刚刚取出的单词列表，接着做一个判断： 如果字典中 key 已经出现了这个单词
#那么它对应的value，也就是出现次数就+1；如果这个单词没出现过，就直接插入这个单词及value为1到字典中
list1=list(input('请输入英文文本:').split(' '))
print(list1)
dict1={}
length=len(list1)
print(length)
i=0
while(i<length):
    str1=list1[i]
    if(str1 not in dict1.keys()):
        dict1[str1]=1
    elif(str1 in dict1.keys()):
        dict1[str1]+=1
    i+=1
print(dict1)
print(sorted(dict1.items(),key = lambda x:x[1],reverse = True))
