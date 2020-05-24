#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   exe1.19.py
@Time    :   2020/04/21 00:12:10
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#将一个文件夹下的某个文件,拷贝到另外一个文件夹下去
#写一个copy函数，接受两个参数，第一个参数是源文件的位置，第二个参数是目标位置，将源文件copy到目标位置。
#还需要判断一下这个文件之前是否存在;  读源文件的内容; 创建目标文件; 读到的内容,再写入到目标文件

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
