#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   4.py
@Time    :   2020/04/14 23:21:10
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here

#在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
#将当前img目录所有以.png结尾的后缀名改为.jpg.
import os
#os.mkdir('img')  #创建文件夹
'''
for i in range(0,10):
    stri=str(i)
    str1=stri+'4G5.png'
    f=open('/Users/maxiaoyu/Desktop/python/img/'+str1,'w') #创建10个.png文件
    f.close()
'''
#if filename in img:
for maindir, subdir, file_name_list in os.walk('/Users/maxiaoyu/Desktop/python/img'):
    print("3:",file_name_list)  #当前主目录下的所有文件
for filename in file_name_list:
    if filename.endswith(".png"):
        basefilename=os.path.splitext(filename)[0]
        oldname=os.path.join(maindir+'/'+basefilename+'.png')
        newname=os.path.join(maindir+'/'+basefilename+'.jpg')
        os.rename(oldname,newname)