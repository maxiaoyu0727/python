#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   exe1.15-.py
@Time    :   2020/03/26 16:41:21
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here

#将10个同同学成绩排序的问题,用 sort函数来实现;这个10个同学的成绩,用列表存放, 列表里面每个元素是一个元组;
'''
import random
score = [random.randint(40,100) for x in range(10)]
print(score)
dic1 = { }
for i in range(len(score)):
    dic1[i] = score[i]
print(dic1)
dic2 = sorted(dic1.items(), key=lambda item: item[1], reverse=True)
for key,value in dic2:
    print(key ,":",value)
'''

'''
a = 1
b = 2
a,b = b,a
print("a的值为:",a)
print("b的值为:",b)
'''

'''
def sum(a,b):
    total=a+b
    return total
sum1=sum(1,2)
print(sum1)
'''

#练习os.path 相关方法的使用
'''
import os
print(os.getcwd())#当前工作目录
current_work_dir = os.path.dirname(__file__)#当前文件所在目录
print(current_work_dir)
#os.mkdir('test')
#os.rename('test','newtest')
os.rmdir('newtest')

import os
print(os.getcwd())
print( os.path.basename('/Users/maxiaoyu/Desktop/python/exe1.15-.py') )   # 返回文件名
print( os.path.dirname('/Users/maxiaoyu/Desktop/python/python3') )    # 返回目录路径
print( os.path.split('/Users/maxiaoyu/Desktop/python/exe1.15-.py') )  # 分割文件名与路径
print( os.path.join('root','test','runoob.txt') )  # 将目录和文件名合成一个路径

import time
print(os.getcwd())
print( os.path.getctime('/Users/maxiaoyu/Desktop/python') )
print( time.gmtime(os.path.getmtime('/Users/maxiaoyu/Desktop/python')) ) 
'''

#构造上述文件结构,分别在指定位置打开文件进行写入操作

'''import os

print(os.getcwd())
f=open('test.txt','r')
f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
print(f.read())
f.close()
'''

#练习3:   一个文件内容的如下,请读取文件的内容, 并输出;
#            姓名      学号      分数
#            张三      101       78
#            李四      102       87
#            王五      103       83
'''
with open('test.txt','r') as f:
    print(f.read())
'''

#一个文件内容的如下,请按照行读取文件的内容,  将分数排序后输出到另外一个文件中:
#            姓名      学号      分数
#            张三      101         78
#            李四      102         87
#            王五      103        83
'''
i=0
list1=[]
with open('test.txt','r') as f:
    for line in f.readlines():
        print(line.strip())
'''

#给定一个字典,保存了5个同学的学号,姓名,年龄;使用pickle模块将数据对象保存到文件中去;
'''
import pickle
dic1={101:['ma',11],102:['xiao',12],103:['yu',13],104:['am',14],105:['uy',15]}
print(dic1)
with open('test.txt','ab+') as f:
    pickle.dump(dic1, f)
'''

#读取文件里面的内容(包含中文), 进行打印输出显示
'''
with open('test.txt','r') as f:
    print(f.readlines())
'''

#构造文件结构
import os
'''
os.mkdir('testfile')
path=r'/Users/maxiaoyu/Desktop/python/testfile'
os.mkdir(path+'/a_file')
os.mkdir(path+'/b_file')
f=open('/Users/maxiaoyu/Desktop/python/testfile/b_file/a.txt','w')
f.close()
'''

#读取文件里面的内容(包含中文), 进行打印输出显示;注意:请设置文件的不同编码格式进行观察
f=open('/Users/maxiaoyu/Desktop/python/test1.txt','r')
str1=f.read()
print(str1)
f.close()

