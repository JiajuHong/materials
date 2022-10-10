#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import random

import pymysql
from faker import Faker

f = Faker('zh_CN')


def create_data1():
    name = f.name()
    phone = f.phone_number()
    email = f.email()
    sex = random.choice(["男", "女"])
    register_time = f.date_time_this_century()
    recent_time = f.date_time_this_century()
    credits = random.choice(["高", "中", "低"])
    job = f.job()
    a = """保险业、采矿、能源、餐饮、宾馆、电讯业、房地产、服务、服装业、公益组织、广告业、航空航天、化学、健康、保健、建筑业、教育、培训、计算机、金属冶炼、警察、消防、会计、美容、媒体、出版、木材、造纸、零售、批发、农业、旅游业、司法、律师、司机、体育运动、学术研究、演艺、医疗服务、艺术、设计、银行、金融、因特网、音乐舞蹈、邮政快递、运输业、政府机关、机械制造、咨询"""
    industry = random.choice(a.split("、"))
    place = f.city_name()
    company = f.company()
    value = credits = random.choice(["高", "中", "低"])

    # 建立连接对象
    connection = pymysql.connect(host='192.168.1.7',
                                 port=3306,
                                 user='root',
                                 password='root',
                                 db='materials',
                                 )

    cursor = connection.cursor()
    sql = f"""INSERT INTO login_customer(`name`,`phone`,`email`,`sex`,`register_time`,`recent_time`,`credibility`,`job`,`industry`,`place`,`company`,`value`) \
    VALUES ("{name}","{phone}","{email}","{sex}","{register_time}","{recent_time}","{credits}","{job}","{industry}","{place}","{company}","{value}")"""
    cursor.execute(sql)

    connection.commit()
    cursor.close()  # 关闭游标
    connection.close()  # 关闭连接


# for i in range(100):
#     create_data()

def create_data2():
    order_name = random.choice(
        ["办公设备", "电脑耗材", "办公用纸", "财务用品", "测绘用品", "日用劳保", "商务礼品", "飞行器材", "军工设备", "东风设备", "恒河水", "福岛营养水", "野生奥特曼",
         "野生葫芦娃", "水晶琉璃奥特曼"])
    Signed_time = f.date_time_this_century()
    cost = random.randint(3000, 5000)
    price = random.randint(3000, 4000)
    order_status = random.randint(1, 3)
    customer_id = random.randint(727, 926)
    # 建立连接对象
    connection = pymysql.connect(host='192.168.1.7',
                                 port=3306,
                                 user='root',
                                 password='root',
                                 db='materials',
                                 )
    cursor = connection.cursor()
    sql = f"""INSERT INTO login_order(`order_name`,`Signed_time`,`price`,`order_status`,`customer_id`, `cost`) values ("{order_name}","{Signed_time}","{price}","{order_status}","{customer_id}", "{cost}")"""

    cursor.execute(sql)
    connection.commit()
    cursor.close()  # 关闭游标
    connection.close()  # 关闭连接


def create_data3():
    name = f.company()
    category = random.choice(
        ["食品原料", "五金器材", "酒水饮料", "电脑配件", "日用劳保", "商务礼品"])
    city = f.city_name()
    phone = f.phone_number()
    time = f.date_time_this_century()

    # 建立连接对象
    connection = pymysql.connect(host='192.168.1.7',
                                 port=3306,
                                 user='root',
                                 password='root',
                                 db='materials',
                                 )

    cursor = connection.cursor()
    sql = f"""INSERT INTO login_supplier(`name`, `category`, `city`, `phone`, `time`) \
        VALUES ("{name}", "{category}", "{city}","{phone}","{time}")"""
    cursor.execute(sql)

    connection.commit()
    cursor.close()  # 关闭游标
    connection.close()  # 关闭连接


for i in range(100):
    create_data2()
    # create_data1()
#     create_data1()
