#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   1.py
@Time    :   2020/03/27 00:52:49
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，将读入的字符串存于列表;
#然后将列表里面的内容写入到文件input.txt中；

def input_L():
    L = []
    while True:
        info = input('>>>')
        if not info:
            return L
        L.append(info)
def write_file(L):
    try:
        f = open("/Users/maxiaoyu/Desktop/python/pythonprojects/input.txt","w")
        for x in L:
            f.write(x)
            f.write('\n')
        f.close()
    except IOError:
        print("write error;")
        
L=input_L()
write_file(L)


f=open("/Users/maxiaoyu/Desktop/python/pythonprojects/input.txt","r")
str1=f.read()
print(str1)
f.close()
