#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   1.py
@Time    :   2020/05/14 19:03:50
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
#实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;

class dog:
    doglist=[{'colour':'red','num':10,'price':1000},{'colour':'black','num':9,'price':1200},{'colour':'white','num':8,'price':1500}]
    @classmethod
    def sell(cls):  
        print('本店出售red,white,black颜色的狗狗')
        colour=input('请输入想要购买的颜色:')
        if colour=='red':
            reddic=cls.doglist[0]
            print('red颜色狗狗的价钱为：',reddic['price'])
            reddic['num']-=1
        if colour=='black':
            blackdic=cls.doglist[1]
            print('red颜色狗狗的价钱为：',blackdic['price'])
            blackdic['num']-=1
        if colour=='white':
            whitedic=cls.doglist[0]
            print('red颜色狗狗的价钱为：',whitedic['price'])
            whitedic['num']-=1

print('red有{}只，black有{}只，white有{}只'.format(dog.doglist[0]['num'],dog.doglist[1]['num'],dog.doglist[2]['num']))
dog1=dog()
dog1.sell()
dog1.sell()
dog1.sell()
print('red剩下{}只，black剩下{}只，white剩下{}只'.format(dog1.doglist[0]['num'],dog1.doglist[1]['num'],dog1.doglist[2]['num']))