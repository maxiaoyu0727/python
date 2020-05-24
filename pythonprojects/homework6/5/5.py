#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   5.py
@Time    :   2020/05/14 22:05:00
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
'''
请写一个小游戏，人狗大站;  规则:
1 2个角色，人和狗，游戏开始后，生成2个人，3条狗，人狗互相交替对战(注意,人只能打狗,  狗也只会咬人); 
  人的打击力为10;  初始化血为100;    狗的攻击力为 15; 初始化血为80;
2 人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。血为0的话,表示死亡,退出游戏;
  人和狗的攻击力,都会因为被咬, 或者被打而降低(人被咬一次,打击力降低2;  狗被打一次,攻击力降低3);
3  对战规则: 
 A 随机决定,谁先开始攻击; 
 B 一方攻击完毕后, 另外一方再开始攻击;  攻击的目标是随机的(比如, 人要打狗了, 随机找一条血不为0的狗攻击);
 C 每次攻击, 双方只能安排一个人,或者一条狗进行攻击;
提示：注意组织代码的方式；狗类用一个单独的py文件； 人用一个单独的py文件；
 在写一个fight模块（也用类来组织；在这个模块中，导入人和狗模块中编写好的方法）
'''

   
import random
from dog import dogclass
from people import peopleclass


def show(dogs,people):
    for i in range(1,len(dogs)+1):
        print('第{}只狗的血量为：{},攻击力为：{}'.format(i,dogs[i-1].blood,dogs[i-1].attack))
    for i in range(1,len(people)+1):
        print('第{}个人的血量为：{},攻击力为：{}'.format(i,people[i-1].blood,people[i-1].attack))

def fight():
    print('人狗大战')
    dogs=[]
    people=[]
    for i in range(0,3):
        dog1=dogclass()
        dogs.append(dog1)
    for i in range(0,2):
        person=peopleclass()
        people.append(person)
    show(dogs,people)
    order=random.choice([0,1])
    while(len(dogs)>0 and len(people)>0):
        print('✨'*40)
        if(order==1):
            print('狗狗攻击人')
            dogs.sort(key=lambda x:x.attack,reverse=True)
            a_dog=dogs[0]
            n=random.randint(0,len(people)-1)
            a_people=people[n]
            a_people.attacked(a_dog)
            if(a_people.blood<=0):
                people.pop(n)
            order=0


        else:
            print("人攻击狗狗")
            people.sort(key=lambda x:x.attack,reverse=True)
            a_people=people[0]
            n=random.randint(0,len(dogs)-1)
            a_dog=dogs[n]
            a_dog.attacked(a_people)
            if(a_dog.blood<=0):
                dogs.pop(n)
            order=1
        show(dogs,people)
        attacklist=[]
        for i in dogs:
            attacklist.append(i.attack)
        for i in people:
            attacklist.append(i.attack)
        attackflag=len(dogs)+len(people)
        for i in attacklist:
            if(i<=0):
                attackflag-=1
        if(attackflag==0):
            print('平局')
            break
    if(len(dogs)<=0):
        print("人取得胜利！")
    elif(len(people)<=0):
        print("狗取得胜利！")
    
fight()