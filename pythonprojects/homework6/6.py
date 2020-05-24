#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   6.py
@Time    :   2020/05/14 23:16:13
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#用面向对象,实现一个学生Python成绩管理系统;
#学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
#实现对学生信息及成绩的增,删,改,查方法;

class student:
    def __init__(self,class1='',num=' ',name=' ',score=0):
        self.class1=class1
        self.num=num
        self.name=name
        self.score=score
    def add(self):
        with open('/Users/maxiaoyu/Desktop/python/pythonprojects/homework6/score.txt','a') as f:
            f.write('\n'+self.class1+' '+self.num+' '+self.name+' '+self.score+'\n')
    def delete(self,num):
        data=[]
        with open('/Users/maxiaoyu/Desktop/python/pythonprojects/homework6/score.txt')as f:
            for line in f.readlines():
                if(line.split(' ')[1]==num):
                    continue
                else:
                    data.append(line)
        with open('/Users/maxiaoyu/Desktop/python/pythonprojects/homework6/score.txt','w')as f:
                for i in data:
                    f.write(i)

    def search(self,num):
        with open('/Users/maxiaoyu/Desktop/python/pythonprojects/homework6/score.txt')as f:
            for line in f.readlines():
                if(line.split(' ')[1]==num):
                    print('学生信息为：',line)
                    break
            else:
                    print('学号不存在')
                    print(' ')


def scoresystem():
    while(True):
        print('欢迎来到学生成绩管理系统')
        print('1.添加学生成绩信息')
        print('2.删除学生成绩信息')
        print('3.修改学生信息')
        print('4.查询学生信息')
        choice=int(input('请输入想要进行的操作：'))
        if(choice==1):
            class1=input('请输入学生班级：')
            num=input('请输入学生学号：')
            name=input('请输入学生姓名：')
            score=input('请输入学生分数：')
            stu=student(class1,num,name,score)
            stu.add()

        elif(choice==2):
            num=input('请输入想要删除的学生学号：')
            stu=student()
            stu.delete(num)

        elif(choice==3):
            num=input('请输入想要修改的学生学号：')
            class1=input('请输入新的学生班级：')
            name=input('请输入新的学生姓名：')
            score=input('请输入新的学生分数：')
            stu=student(class1,num,name,score)
            stu.delete(num)
            stu.add()
        
        elif(choice==4):
            num=input('请输入学生学号进行查询：')
            stu=student()
            stu.search(num)

scoresystem()
       