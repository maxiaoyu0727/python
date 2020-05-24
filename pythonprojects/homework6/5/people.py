#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   people.py
@Time    :   2020/05/16 23:48:27
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here

class peopleclass:
    num=1
    def __init__(self):
        self.num=peopleclass.num
        self.attack=10
        self.blood=100
        peopleclass.num+=1

    def attacked(self,dog):
        if(self.attack>=2):
            self.attack-=2
        self.blood-=dog.attack
