#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   exe0408-.py
@Time    :   2020/04/27 23:55:03
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#定义一个dog类(颜色, 名称), 里面有一个狗叫的方法; 不同的狗叫声可能不一样;  
#然后实例化几条狗, 然后统计实例化狗的数量

class dog:
    colour='white'
    name='wangcai'
    count=0
    def __init__(self,colour,name):
        self.colour=colour
        self.name=name
        dog.count+=1
    def voice(self):
        if self.colour=='black':
            print('汪汪')
        if self.colour=='white':
            print('wangwangwang')
        elif self.colour!='black' and self.colour!='white':
            print('其他颜色的狗不会叫')


dog1=dog('white','wangcai')
dog2=dog('black','xiaobai')
dog3=dog('red','xiaohong')
dog1.voice()
dog2.voice()
dog3.voice()
print(dog.count)
