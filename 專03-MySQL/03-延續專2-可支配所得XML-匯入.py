#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"
"""
家庭收支調查-所得收入者職業別平均每人"所得收入總計" ↓  2020-10-27
https://data.gov.tw/dataset/131148
家庭收支調查-所得收入者職業別平均每人"非消費支出" ↓  2020-11-18
https://data.gov.tw/dataset/132281
家庭收支調查-所得收入者職業別平均每人"可支配所得" ↓ 2020-09-23
https://data.gov.tw/dataset/130027
主要欄位 ↓
Year、臺灣地區、民意代表及主管及經理人員、專業人員、技術員及助理專業人員、
事務支援人員、服務及銷售工作人員、農林漁牧業生產人員、技藝有關工作人員、
機械設備操作及組裝人員、基層技術工及勞力工、其他
"""

import sys
from xml.etree import ElementTree
import urllib.request as httplib  # 3.x

import pymysql as MySQLdb             #  pip install MySQLdb
db = MySQLdb.connect(host="127.0.0.1", user="admin", passwd="admin", db="mydatabase")
cursor = db.cursor()

try:
    # 家庭收支調查 - 所得收入者職業別平均每人"所得收入總計" 最後更新時間 2020 - 10 - 27
    # url = "https://www.dgbas.gov.tw/public/data/open/localstat/086-%E6%89%80%E5%BE%97%E6%94%B6%E5%85%A5%E8%80%85%E8%81%B7%E6%A5%AD%E5%88%A5%E5%B9%B3%E5%9D%87%E6%AF%8F%E4%BA%BA%E6%89%80%E5%BE%97%E6%94%B6%E5%85%A5%E7%B8%BD%E8%A8%88.xml"
    # 非消費性支出
    # url =https://www.dgbas.gov.tw/public/data/open/localstat/088-%E6%89%80%E5%BE%97%E6%94%B6%E5%85%A5%E8%80%85%E8%81%B7%E6%A5%AD%E5%88%A5%E5%B9%B3%E5%9D%87%E6%AF%8F%E4%BA%BA%E9%9D%9E%E6%B6%88%E8%B2%BB%E6%94%AF%E5%87%BA.xml
    # 可支配所得
    url="https://www.dgbas.gov.tw/public/data/open/localstat/085-%E6%89%80%E5%BE%97%E6%94%B6%E5%85%A5%E8%80%85%E8%81%B7%E6%A5%AD%E5%88%A5%E5%B9%B3%E5%9D%87%E6%AF%8F%E4%BA%BA%E5%8F%AF%E6%94%AF%E9%85%8D%E6%89%80%E5%BE%97.xml"
    req = httplib.Request(url)
    reponse = httplib.urlopen(req)
    if reponse.code == 200:
        if (sys.version_info > (3, 0)):
            # contents=reponse.read().decode(reponse.headers.get_content_charset())
            contents = reponse.read().decode("UTF-8")
        else:
            contents = reponse.read()

        print(contents)
        root = ElementTree.fromstring(contents)

        t0 = root.findall("Data")
        t1 = root.findall("Data/Year")
        t2 = root.findall("Data/臺灣地區")
        t3 = root.findall("Data/民意代表及主管及經理人員")
        t4 = root.findall("Data/專業人員")
        t5 = root.findall("Data/技術員及助理專業人員")
        t6 = root.findall("Data/事務支援人員")
        t7 = root.findall("Data/服務及銷售工作人員")
        t8 = root.findall("Data/農林漁牧業生產人員")
        t9 = root.findall("Data/技藝有關工作人員")
        t10 = root.findall("Data/機械設備操作及組裝人員")
        t11 = root.findall("Data/基層技術工及勞力工")
        t12 = root.findall("Data/其他")

        #listYear = []
        #for x in range(0, len(t0)):
        #    listYear.append(t1[x].text)

        # 印出所有資料
        for x in range(0, len(t0)):
            print("年份:", t1[x].text)
            print("台灣地區平均每人所得收入總計:", t2[x].text)
            print("   ")
            print("民意代表及主管及經理人員:", t3[x].text)
            print("專業人員:", t4[x].text)
            print("技術員及助理專業人員:", t5[x].text)
            print("事務支援人員:", t6[x].text)
            print("服務及銷售工作人員:", t7[x].text)
            print("農林漁牧業生產人員:", t8[x].text)
            print("技藝有關工作人員:", t9[x].text)
            print("機械設備操作及組裝人員:", t10[x].text)
            print("基層技術工及勞力工:", t11[x].text)
            print("其他:", t12[x].text)
            print("----------------------------")
            print("   ")

        for x in range(0,len(t0)):
            str1 = "INSERT INTO `income` (`id`, `year`, `taiwan`, `supervisor`, `professionals`, `assistant`, `support`, `service`, `production`, `artisan`, `assembler`, `labor`, `other`)" + \
                   " VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]','[value-7]','[value-8]','[value-9]','[value-10]','[value-11]','[value-12]','[value-13]')"
            str1 = str1.replace("[value-1]", "null")
            str1 = str1.replace("[value-2]", t1[x].text)
            str1 = str1.replace("[value-3]", t2[x].text)
            str1 = str1.replace("[value-4]", t3[x].text)
            str1 = str1.replace("[value-5]", t4[x].text)
            str1 = str1.replace("[value-6]", t5[x].text)
            str1 = str1.replace("[value-7]", t6[x].text)
            str1 = str1.replace("[value-8]", t7[x].text)
            str1 = str1.replace("[value-9]", t8[x].text)
            str1 = str1.replace("[value-10]", t9[x].text)
            str1 = str1.replace("[value-11]", t10[x].text)
            str1 = str1.replace("[value-12]", t11[x].text)
            str1 = str1.replace("[value-13]", t12[x].text)
            # print(str1)
            cursor.execute(str1)

        db.commit()
        db.close()
        print("====資料量====")
        print(len(t0))
except:
    print("error")
