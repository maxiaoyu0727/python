#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   5.py
@Time    :   2020/04/15 00:20:49
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#文件编程小项目
import os

f1=open('/Users/maxiaoyu/Desktop/python/pythonprojects/Blowing in the wind.txt','w')
f1.write('How many roads must a man walk down \n')
f1.write('Before they call him a man \n')
f1.write('How many seas must a white dove sail \n')
f1.write('Before she sleeps in the sand \n')
f1.write('How many times must the cannon balls fly \n')
f1.write('Before they\'re forever banned \n')
f1.write('The answer my friend is blowing in the wind \n')
f1.write('The answer is blowing in the wind\n')
f1.close()
 
#在文件头部插入歌曲名
f2=open('/Users/maxiaoyu/Desktop/python/pythonprojects/Blowing in the wind.txt','r+')
l1 =f2.readlines()
l1.insert(0,'Blowin\'in the wind\n')#在第一行添加歌曲名
f2.seek(0,0)#将文件指针移动到文件开头处
f2.writelines(l1)
f2.close()
 
#在歌名后插入歌手名
f3=open('/Users/maxiaoyu/Desktop/python/pythonprojects/Blowing in the wind.txt','r+')
l2 =f3.readlines()
l2.insert(1,'——Bob Dylan\n')#在第一行添加歌手名
f3.seek(0,0)#将文件指针移动到文件开头处
f3.writelines(l2)
f3.close()
 
#在文件末尾加上字符串“1962 by Warner Bros. Inc.” 
f4=open('/Users/maxiaoyu/Desktop/python/pythonprojects/Blowing in the wind.txt','a')
f4.write('1962 by Warner Bros. Inc.')
f4.close()
 
#在屏幕上打印文件内容
f5=open('/Users/maxiaoyu/Desktop/python/pythonprojects/Blowing in the wind.txt','r')
l4 =f5.readlines()
for i in range(0,len(l4)):
    if 1<i<len(l4)-1:
        print('\t'+l4[i])
    else:
        print('\t\t'+l4[i])
f5.close()