#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   2.py
@Time    :   2020/05/27 21:37:16
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）
#（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
#使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；


import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","root","27718872maxiaoyu","exe1" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
 
# 创建表
def build():
    build_sql = """CREATE TABLE message_board1
            (
            id  VARCHAR(20) NOT NULL,
            subject  VARCHAR(20),
            name VARCHAR(20),
            time date,
            is_delete int
            )"""
    cursor.execute(build_sql)
#增
def add():
    add_sql1 = "insert into message_board1 values ('101','hello','maxiaoyu',20200101,0)"
    add_sql2 = "insert into message_board1 values ('102','bye','maxiaoyu2',20200102,1)"
    cursor.execute(add_sql1)
    cursor.execute(add_sql2)
#删
def delete():
    delete_sql = "delete from message_board1 where id='102'"
    cursor.execute(delete_sql)

#改
def update():
    update_sql = "update message_board1 set time=20200102 where id='101'"
    execute(update_sql)

#查
def select():
    select_sql="select * from message_board1"
    cursor.execute(select_sql)
    result=cursor.fetchall()
    print(result)


build()
add()


db.commit()
 
# 关闭数据库连接
cursor.close()
db.close()