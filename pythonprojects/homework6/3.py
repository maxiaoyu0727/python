#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   3.py
@Time    :   2020/05/14 21:04:37
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#定义一个字典类：dictclass。完成下面的功能：
#dict = dictclass({你需要操作的字典对象})
#1 删除某个key
#del_dict(key)
#2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
#get_dict(key)
#3 返回键组成的列表：返回类型;(list)
#get_key()
#4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
#update_dict({要合并的字典})

class dictclass:
    dic={}
    def __init__(self,dic):
        self.dic=dic
    def del_dict(self,key):
        del dic[key]
    def get_dict(self,key):
        if key in dic:
            return dic[key]
        else:
            return 'not found'
    def get_key(self):
        return dic.keys()
    def update_dict(self,dic2):
        dic.update(dic2)
        return(dic)

dic={'colour':'red','num':10,'price':1000}
dic2={'colour1':'black','num1':9,'price1':1200}
dict1=dictclass(dic)
dict1.del_dict('colour')
print(dict1.get_dict('colour'))
print(dict1.get_key())
print(dict1.update_dict(dic2))
