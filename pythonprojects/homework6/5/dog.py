#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   dog.py
@Time    :   2020/05/16 23:48:16
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here

class dogclass:
    num=1
    def __init__(self):
        self.num=dogclass.num
        self.attack=15
        self.blood=80
        dogclass.num+=1
    def attacked(self,people):
        if(self.attack>=3):
            self.attack-=3
        self.blood-=people.attack
