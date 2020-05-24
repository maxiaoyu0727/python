#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   6.py
@Time    :   2020/04/25 23:28:03
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小; 输出格式效果如下:
#   名称         日期                   类型（文件夹或者 文件）       大小
import os
import time
def isfile_folder(path):
    if(os.path.isfile(path)==True):
        return '文件'
    else:
        return '文件夹'

path='/Users/maxiaoyu/Desktop/python/pythonprojects'
dirlist=os.listdir(path)
List=[['名称','日期','类型（文件夹或者文件）','大小']]
for file in dirlist:
    a=[]
    path1=os.path.join(path,file)
    a.append(file)
    a.append(time.ctime(os.path.getctime(path1)))
    a.append(isfile_folder(path1))
    a.append(os.path.getsize(path1))
    List.append(a)
tplt="{0:{4}^10}\t{1:{4}^10}\t{2:{4}^10}\t{3:^10}"
for l in List:
    print(tplt.format(l[0],l[1],l[2],l[3],chr(12288)))

