#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   4.py
@Time    :   2020/03/15 00:39:46
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here

#写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果;
def judge():
    list1=list(input("请输入字符串:"))
    print(list1)
    letter=0
    number=0
    space=0
    other=0
    i=0
    for x in list1:
        str1=str(list1[i])
        if str1.isalpha():
            letter+=1
        elif str1.isdigit():
            number+=1
        elif str1.isspace():
            space+=1
        else:
            other+=1
        i+=1
    print("字符串中字母有{}个".format(letter))
    print("字符串中数字有{}个".format(number))
    print("字符串中空格有{}个".format(space))
    print("字符串中其他字符有{}个".format(other))
judge()