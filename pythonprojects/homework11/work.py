#在51job网站上，爬取2020年发布的Python开发工程师的职位的薪酬，计算北京地区改职位的平均薪酬；

import requests
from lxml import etree
import re
from datetime import datetime
import pymysql


# 打开数据库连接
db = pymysql.connect("localhost","root","27718872maxiaoyu","exe1" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

 
# 创建表
def build():
    cursor.execute("DROP TABLE IF EXISTS salary")
    build_sql = """CREATE TABLE salary
            (
            jobname  VARCHAR(255),
            company  VARCHAR(255),
            salary VARCHAR(255)
            )"""
    cursor.execute(build_sql)


#增
def add():
    for i in range(1,4):
        url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='.format(i)
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        }
        r = requests.get(url,headers=headers)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        
        e = etree.HTML(r.text)

        jobnames = e.xpath('//*[@id="resultList"]/div/p/span/a/text()')
        companys = e.xpath('//*[@id="resultList"]/div/span[1]/a/text()')
        sal = e.xpath('//div[@class="dw_table"]/div[@class="el"]/span[@class="t4"]')
        salarys = [i.text for i in sal]
        for jobname,company,salary in zip(jobnames,companys,salarys):
            jobname=str(jobname.strip())
            company=str(company)
            salary=str(salary)
            data = {
                'jobname':jobname.strip(),
                'company':company,
                'salary':salary
            }
            print(data)
            #print(type(jobname),type(company),type(salary))
            add_sql1 = "insert into salary values ('{}','{}','{}')".format(jobname,company,salary)
            cursor.execute(add_sql1)
        print('\n')
    print('～～～～～～～～～～～～～～～～～～～～～～～～～')
    print('～～～～～～～～～～～～～～～～～～～～～～～～～')
    print('数据已存储到exe数据库中的salary表中')
    print('～～～～～～～～～～～～～～～～～～～～～～～～～')
    print('～～～～～～～～～～～～～～～～～～～～～～～～～')
    print('\n')


def average_salary():
    total_salary=0
    count=0
    beijing_average_salary=0
    select_sql="select salary from salary"
    cursor.execute(select_sql)
    result=cursor.fetchall()
    for i in result:
        salary1=str(i[0])
        salary_list=[]
        for s in re.findall(r'\d+(?:\.\d+)?', salary1):
            salary_list.append(float(s) )
        #print(salary_list)
        time_unit=salary1[-1:]
        money_unit=salary1[-3:-2]
        every_average_salary=0
        #print(time_unit)
        #print(money_unit)
        if(time_unit=='月'):
            every_average_salary=(salary_list[0]+salary_list[1])/2
        if(time_unit=='天'):
            every_average_salary=salary_list[0]*0.003
        if(time_unit=='年'):
            every_average_salary=(salary_list[0]+salary_list[1])/24
        if(money_unit=='千'):
            every_average_salary=every_average_salary/1000
        #print(every_average_salary)
        total_salary+=every_average_salary
        count+=1

    beijing_average_salary=total_salary/count
    print('\n')
    print('**************************************************')
    print('**************************************************')
    print('北京地区python开发工程师的薪资平均为：','%.2f'%(beijing_average_salary),'万元/月')
    print('**************************************************')
    print('**************************************************')
    print('\n')
    

build()
add()
average_salary()

db.commit()
 
# 关闭数据库连接
cursor.close()
db.close()