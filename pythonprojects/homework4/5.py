#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   5.py
@Time    :   2020/04/25 23:26:56
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#通过Python来模拟实现一个txt文件的拷贝过程
import os
import shutil
def copy(path1,path2):
    tuple1=os.path.split(path1)
    filename=tuple1[1]
    if(os.path.exists(path1)):
        with open(path1,'r') as f:
            f1=open(path2+filename,'w') 
            f1.write(f.read())
            f1.close()
    else:
        print('文件不存在')
path1='/Users/maxiaoyu/Desktop/python/pythonprojects/exe1.00-1.12.py'
path2='/Users/maxiaoyu/Desktop/python/testfile/'
copy(path1,path2)