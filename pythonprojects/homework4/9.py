#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   9.py
@Time    :   2020/04/27 00:24:56
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#从网络上下载一张图片，保存到计算机的指定目录；（requests和os模块）

import requests
import os
pic_path="http://img4.imgtn.bdimg.com/it/u=511206154,854776760&fm=214&gp=0.jpg"
into_path='/Users/maxiaoyu/Desktop/python'
path=into_path+pic_path.split('/')[-1]

r=requests.get(pic_path)
r.raise_for_status()
with open(path,'wb') as f:
    f.write(r.content)
    f.close()
    print("图片保存成功")
