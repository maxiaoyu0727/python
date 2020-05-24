#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   test.py
@Time    :   2020/03/10 22:28:13
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here


#输出字符串
'''
print("我爱你中国！")
'''

#定义不同字符串并且输出，加上转义字符
'''
a="my name is maxiaoyu"
b="i am a girl"
c="i am 19"
d=a+b+c
print(d)

print("maxiaoyu",'\n')
print("maxiaoyu",r'\n')
'''

#定义一个字符串,分别进行查找某个字符串是否包含在这个字符串里面; 进行某个字符串的替换; 打印字符串的长度
'''
str="my name is maxiaoyu"
if ('y' in str) :
     print("y在该字符串中")
name2="maxiaoyu2"
str2=f'her name is {name2}'
print(len(str),"\n",len(str2))
print("o在字符串中的位置为",str.find('o'))
'''

#用列表定义10个同学的成绩,输出最高分,最低分,总分和平均值
'''
list=[97,94,93,98,100,95,92,96,91,99]
print("最高分为：",max(list))
print("最低分为：",min(list))
print("总分为：",sum(list))
print("平均分为：",sum(list)/len(list))
'''

#定义元组,进行基本的操作(元组的基本运算,元素的输出,内置函数的使用); 定义一个元组,来保存成绩,输出最高分;
'''
tup1=(1,2,3)
tup2=("one",'two','three')
tup3=tup1+tup2
tup4=tup1*3
print(tup3,'\n',tup4,'\n',tup2[1:3])
print(len(tup3))
print(max(tup1))

score=(98,96,100,99,97)
print(max(score))
'''

#定义一个字典,存放某个同学的信息(学号,姓名,班级,年龄);   再定义另外一个字典,存放5个同学的学号,姓名信息;通过键来访问相应的数据; 或者整体输出
'''
dict1={'number':'123','name':'maxiaoyu','class':2,'age':19}
dict2={'121':'lily','122':'lisa','123':'maxioayu','124':'tom','125':'jack'}
print(dict1['name'])
print(dict2['124'])
print(dict1)
'''

#字典的元素的增加, 修改,删除; 并观察输出
'''
dict={'name':'maxiaoyu','age':19,'number':123}
print(dict)
dict['age']=20
print(dict)
dict['school']='ncepu'
print(dict)
del dict['number']
print(dict)
'''

#定义一个集合类型的变量(用2种方法初始化),然后进行相应的 元素的操作
'''
set1=set(('apple','banana','orange','pear'))
set2={1,2,3,4}
print(set1)
set1.update([1,2,3])
print(set1)
set1.remove(3)
print(set1)
print(len(set1))
set1.clear()
print(set1)
print(1 in set2)
'''

#将控制台输入的字符串,转换成元组, 并输出显示;  
'''
str1=input("请输入内容：")
tup=tuple(str1)
print(tup)
'''

#提示输入需要购买的苹果的重量(斤),然后提示输入每斤的价格,请计算应支付的总价,并打印提示输出;
'''
weight=int(input("请输入需要购买的苹果的重量（斤）:"))
print("请注意，每斤的价格为5元")
price=5
money=weight * price
print("应支付的总价为：",money)
'''

#将这4中方式实现的代码分别在vscode上练习一下;
'''
name=input("name:")
age=int(input("age:"))
skill=input("skill:")
salary=int(input("salary:"))
info="name:"+name+" age:"+age+" skill:"+skill+" salary:"+salary
print(info)
info2="name:%s age:%d skill:%s salary:%d"%(name,age,skill,salary)
print(info2)
info3='name:{} age:{} skill:{} salary:{}'.format(name,age,skill,salary)
print(info3)
'''

#创建一个有10个数字的列表,先输出此列表,然后再输出其中为偶数元素
'''
list1=list(range(9))
print(len(list1))
for x in list1:
    print(x)
for x in list1:
    if x % 2==0:
        print(x)
'''