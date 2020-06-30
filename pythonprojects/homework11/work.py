#在51job网站上，爬取2020年发布的Python开发工程师的职位的薪酬，计算北京地区改职位的平均薪酬；

import requests
from lxml import etree
import re
from datetime import datetime
import pymysql
import matplotlib as mpl
import matplotlib.pyplot as plt
import config1


# 打开数据库连接
db = pymysql.connect(host=config1.HOST,user=config1.USERNAME,password=config1.PASSWORD,database=config1.DATABASE )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 创建表
def build():
    #如果表格存在则删除
    cursor.execute("DROP TABLE IF EXISTS salary")
    build_sql = """CREATE TABLE salary
            (
            jobname  VARCHAR(255),
            company  VARCHAR(255),
            salary VARCHAR(255)
            )"""
    cursor.execute(build_sql)


#从网页上爬取数据并存入到数据库中
def add():
    for i in range(1,4):
        url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='.format(i)
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        }
        r = requests.get(url,headers=headers)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        #解析数据
        e = etree.HTML(r.text)
        #爬取职位，公司和薪资三个信息
        jobnames = e.xpath('//*[@id="resultList"]/div/p/span/a/text()')
        companys = e.xpath('//*[@id="resultList"]/div/span[1]/a/text()')
        sal = e.xpath('//div[@class="dw_table"]/div[@class="el"]/span[@class="t4"]')
        salarys = [i.text for i in sal]
        for jobname,company,salary in zip(jobnames,companys,salarys):
            jobname=str(jobname.strip())
            company=str(company)
            salary=str(salary)
            #将爬取到的数据输出
            data = {
                'jobname':jobname.strip(),
                'company':company,
                'salary':salary
            }
            print(data)

            #print(type(jobname),type(company),type(salary))
            #将数据添加到数据库中
            add_sql1 = "insert into salary values ('{}','{}','{}')".format(jobname,company,salary)
            cursor.execute(add_sql1)
        print('\n')
    print('～～～～～～～～～～～～～～～～～～～～～～～～～')
    print('～～～～～～～～～～～～～～～～～～～～～～～～～')
    print('数据已存储到exe数据库中的salary表中')
    print('～～～～～～～～～～～～～～～～～～～～～～～～～')
    print('～～～～～～～～～～～～～～～～～～～～～～～～～')
    print('\n')

#计算平均薪资
def average_salary():
    total_salary=0#工资之和
    count=0#计数器
    beijing_average_salary=0#所求的北京地区平均薪资
    select_sql="select salary from salary"
    cursor.execute(select_sql)
    result=cursor.fetchall()
    for i in result:
        #网页提供的每个职位的薪资是一个范围，现取这个范围的平均值作为该职位的薪资
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

        #同一单位到万元/月
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



#制作饼图，直观显示北京地区python工程师的薪资分布
def pie_photo():
    total_count=0
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
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
        total_count+=1
        if(every_average_salary>=0 and every_average_salary<1):
            count1+=1
        if(every_average_salary>=1 and every_average_salary<2):
            count2+=1
        if(every_average_salary>=2 and every_average_salary<3):
            count3+=1
        if(every_average_salary>=3 and every_average_salary<4):
            count4+=1
        if(every_average_salary>=4):
            count5+=1
    #计算不同薪资的占比
    rate1=count1/total_count
    rate2=count2/total_count
    rate3=count3/total_count
    rate4=count4/total_count
    rate5=count5/total_count
    share=[]
    share.append(rate1)
    share.append(rate2)
    share.append(rate3)
    share.append(rate4)
    share.append(rate5)
    # 生成数据
    labels = ['0-1w', '1-2w', '2-3w', '3-4w', '>4w']

    # 设置分裂属性
    explode = [0.1, 0, 0, 0, 0]
    
    plt.rcParams['font.sans-serif']=['DejaVu Sans'] 
    plt.rcParams['axes.unicode_minus']=False  

    # 制作饼图
    plt.pie(share, explode = explode,
            labels = labels, autopct = '%3.1f%%',
            startangle = 180, shadow = False,
            colors = ['mediumpurple', 'tomato', 'gray', 'mediumseagreen', 'wheat'])

    # 设置标题
    plt.title('Monthly salary of Python engineers in Beijing')
    plt.show()

build()
add()
average_salary()
pie_photo()

db.commit()
 
# 关闭数据库连接
cursor.close()
db.close()