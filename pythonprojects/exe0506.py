#!/Users/maxiaoyu/Desktop/python/evns /py3/bin/python3
#encoding:utf-8
'''
@File    :   exe0506.py
@Time    :   2020/05/27 00:09:04
@Author  :   DesignerA 
@Version :   1.0
@Contact :   DesignerA@qq.com
@WebSite :   www.cnblogs.com/DesignerA
'''
# Start typing your code from here
#创建一个留言板的表（ID，留言主题，留言人，留言时间）4个字段，注意，字段请用英文；
#完成对这个表记录的增，删，改，查询；
#用PyMySQL驱动方式

import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","root","27718872maxiaoyu","exe1" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
 
# 创建表
build_sql = """CREATE TABLE message_board
        (
         id  VARCHAR(20) NOT NULL,
         subject  VARCHAR(20),
         name VARCHAR(20),
         time date
         )"""

#增
add_sql1 = "insert into message_board values ('101','hello','maxiaoyu',20200101)"

add_sql2 = "insert into message_board values ('102','bye','maxiaoyu2',20200102)"

#删
delete_sql = "delete from message_board where id='102'"

#改
update_sql = "update message_board set time=20200102 where id='101'"

#查
select_sql="select * from message_board"

#cursor.execute(build_sql)
#cursor.execute(add_sql1)
#cursor.execute(add_sql2)
#cursor.execute(delete_sql)
#cursor.execute(update_sql)
cursor.execute(select_sql)
result=cursor.fetchall()
print(result)
db.commit()
 
# 关闭数据库连接
cursor.close()
db.close()