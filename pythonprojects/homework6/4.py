#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   4.py
@Time    :   2020/05/14 21:43:49
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
#封装方法，求单个学生的总分，平均分，以及打印学生的信息。

class student():
    def __init__(self,name,age,sex,english,math,chinese):
        self.__name=name
        self.__age=age
        self.__sex=sex
        self.__english=english
        self.__math=math
        self.__chinese=chinese
    def __total(self):
        return(self.__english + self.__math + self.__chinese)
    def __average(self):
        total=self.__english + self.__math + self.__chinese
        return(total/3)
    def printfunc(self):
        print('学生姓名：{}年龄：{}性别：{}英语成绩：{}数学成绩：{}语文成绩：{}总分：{}平均分：{}'.format(self.__name,self.__age,self.__sex,self.__english,self.__math,self.__chinese,self.__total(),self.__average()))

stu1=student('ma',19,'female',99,98,97)
stu1.printfunc()