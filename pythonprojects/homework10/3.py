#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   3.py
@Time    :   2020/05/27 21:49:16
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#对2中的表结构，用SQLAchemy模块来实现同样的操作

from datetime import datetime
from sqlalchemy import Column, String, create_engine,Date,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:27718872maxiaoyu@localhost:3306/exe1')

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'message_board1'
    # 表的结构:
    id = Column(String(20), primary_key=True)
    subject=Column(String(20))
    name = Column(String(20))
    time=Column(Date)
    is_delete=Column(Integer)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


def insert():
    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    new_user = User(id='103',subject='Hi', name='ma2',time=20200201,is_delete=0)
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

def select():
    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user = session.query(User).filter(User.id=='103').one()
    # 打印类型和对象的name属性:
    print('id:', user.id)
    print('subject:',user.subject)
    print('name:', user.name)
    print('time:',user.time)
    print('is_delete:',user.is_delete)
    # 关闭Session:
    session.close()

def delete():
    # 创建session对象:
    session = DBSession()
    session.query(User).filter_by(id='101').delete()
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

def update():
    # 创建session对象:
    session = DBSession()
    session.query(User).filter_by(id='102').update({"subject": "byebye"})
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

#insert()
#select()
#update()
delete()