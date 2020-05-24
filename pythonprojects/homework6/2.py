#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   2.py
@Time    :   2020/05/14 20:06:55
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#定义一个学生Student类。有下面的类属性：
#1 姓名 name
#2 年龄 age
#3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
#类方法：
#1 获取学生的姓名：get_name() 返回类型:str
#2 获取学生的年龄：get_age() 返回类型:int
#3 返回3门科目中最高的分数。get_course() 返回类型:int
#写好类以后，可以定义2个同学测试下:

class student:
    name='mary'
    age=19
    score=(99,99,99)
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return max(self.score)

stu1=student('mike',20,(98,79,69))
print('学生姓名：{}，学生年龄：{}，学生最高分数：{}'.format(stu1.get_name(),stu1.get_age(),stu1.get_course()))

        