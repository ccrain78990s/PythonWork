#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"
"""
家庭收支調查-所得收入者職業別平均每人"所得收入總計" ↓ 
https://data.gov.tw/dataset/131148
家庭收支調查-所得收入者職業別平均每人"非消費支出" ↓  
https://data.gov.tw/dataset/132281
家庭收支調查-所得收入者職業別平均每人"可支配所得" ↓   V 使用資料
https://data.gov.tw/dataset/130027
主要欄位 ↓
Year、臺灣地區、民意代表及主管及經理人員、專業人員、技術員及助理專業人員、
事務支援人員、服務及銷售工作人員、農林漁牧業生產人員、技藝有關工作人員、
機械設備操作及組裝人員、基層技術工及勞力工、其他
"""

import pymysql as MySQLdb             #  pip install MySQLdb
db = MySQLdb.connect(host="127.0.0.1", user="admin", passwd="admin", db="mydatabase")
cursor = db.cursor()

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties  # 中文化

sql = "SELECT * FROM `income`  "
cursor.execute(sql)
result = cursor.fetchall()

print("====資料量====")
print(len(result))

list1,list2,list3=[],[],[]
list4,list5,list6,list7,list8,list9,list10,list11,list12,list13=[],[],[],[],[],[],[],[],[],[]

for record in result:
    # 印出所有資料
    print("ID:", record[0])
    print("年份:", record[1])
    print("台灣地區平均每人所得收入總計:",record[2])
    print("   ")
    print("民意代表及主管及經理人員:", record[3])
    print("專業人員:", record[4])
    print("技術員及助理專業人員:",record[5])
    print("事務支援人員:", record[6])
    print("服務及銷售工作人員:", record[7])
    print("農林漁牧業生產人員:", record[8])
    print("技藝有關工作人員:", record[9])
    print("機械設備操作及組裝人員:", record[10])
    print("基層技術工及勞力工:", record[11])
    print("其他:", record[12])
    print("----------------------------")
    print("   ")
    list1.append(record[0])    # id
    list2.append(record[1])    # 年份
    list3.append(record[2])    # 台灣地區
    list4.append(record[3])    # 民意代表及主管及經理人員
    list5.append(record[4])    # 專業人員
    list6.append(record[5])    # 技術員及助理專業人員
    list7.append(record[6])    # 事務支援人員
    list8.append(record[7])    # 服務及銷售工作人員
    list9.append(record[8])    # 農林漁牧業生產人員
    list10.append(record[9])   # 技藝有關工作人員
    list11.append(record[10])  # 機械設備操作及組裝人員
    list12.append(record[11])  # 基層技術工及勞力工
    list13.append(record[12])  # 其他
# 圖片文字顯示中文
plt.rcParams['font.sans-serif'] = ['SimSun']  # 步驟一（替換sans-serif字型）
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）
# 圖片
plt.figure(figsize=(10,5))
plt.subplot(211)
plt.plot(list2, list3,'r',label='台灣地區')
plt.plot(list2, list4,'y',label='民意代表及主管及經理人員')
plt.title('台灣地區平均 VS 民意代表及主管及經理人員', fontsize = 20)
plt.xlabel('年份')
plt.ylabel('可支配所得')
plt.legend()
#plt.show()

plt.subplot(212)
plt.plot(list2, list3,'r',label='台灣地區')
plt.plot(list2, list13,'b',label='基層技術工及勞力工')
plt.title('台灣地區平均 VS 基層技術工及勞力工', fontsize = 20)
plt.xlabel('年份')
plt.ylabel('可支配所得')
plt.tight_layout()
plt.legend()
plt.show()