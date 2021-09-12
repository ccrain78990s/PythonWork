#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"
"""
臺中市賞樹景點 ↓
https://data.gov.tw/dataset/138706
主要欄位 ↓
項次(臺中市賞樹景點)、縣市別代碼、行政區域代碼、行政區、地點、樹種、花期、備註
"""

import pymysql as MySQLdb             #  pip install MySQLdb
db = MySQLdb.connect(host="127.0.0.1", user="admin", passwd="admin", db="mydatabase")
cursor = db.cursor()

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties  # 中文化

sql = "SELECT * FROM `tree_viewing`  ORDER BY `flowering`  "
cursor.execute(sql)
result = cursor.fetchall()

print("====資料量====")
print(len(result))

list1,list2,list3=[],[],[]
list4,list5,list6=[],[],[]

for record in result:
    # 印出所有資料
    print("ID:", record[0],"項次:", record[1])
    print("地區:", record[2],"地點:",record[3])
    print("樹種:", record[4],"花期:", record[5])
    print("----------------------------")
    print("   ")
    list1.append(record[0])    # id
    list2.append(record[1])    # 項次
    list3.append(record[2])    # 行政區
    list4.append(record[3])    # 地點
    list5.append(record[4])    # 樹種
    list6.append(record[5])    # 花期

# 圖片文字顯示中文

plt.rcParams['font.sans-serif'] = ['SimSun']  # 步驟一（替換sans-serif字型）
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）
# 圖片1
# csfont = {'fontname':'Comic Sans MS'} # 更改字體步驟1
# csfont = {'fontname':'標楷體'} # 更改字體步驟1
plt.figure(figsize=(15,7))
plt.scatter(list5, list6,marker='*',s=300)
# plt.title('110年台中賞樹景點花期', fontsize = 20,**csfont)  # 更改字體步驟2
plt.title('110年台中賞樹景點花期', fontsize = 20)
plt.xlabel('花期')
plt.ylabel('樹種')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=10)

plt.grid(linestyle='-.')
plt.show()
# 圖片2
sql = "SELECT * FROM `tree_viewing` WHERE `area`='北區' ORDER BY `flowering`  "
cursor.execute(sql)
result = cursor.fetchall()

print("====資料量====")
print(len(result))

list1,list2,list3=[],[],[]
list4,list5,list6=[],[],[]

for record in result:
    # 印出所有資料
    print("ID:", record[0],"項次:", record[1])
    print("地區:", record[2],"地點:",record[3])
    print("樹種:", record[4],"花期:", record[5])
    print("----------------------------")
    print("   ")
    list1.append(record[0])    # id
    list2.append(record[1])    # 項次
    list3.append(record[2])    # 行政區
    list4.append(record[3])    # 地點
    list5.append(record[4])    # 樹種
    list6.append(record[5])    # 花期

plt.style.use('dark_background')
plt.figure(figsize=(15,7))
plt.scatter(list4, list5,marker='x',color='r',s=500)        # s=marker大小
plt.title('110年台中【北區】可賞之樹種/花', fontsize = 20)

plt.ylabel('樹種/花')
plt.xticks(rotation=10)
plt.tick_params(axis='x',labelsize=14)
plt.tick_params(axis='y',labelsize=12)
plt.grid(linestyle='--')
plt.show()

########
"""
sql = "SELECT DISTINCT `species` FROM `tree_viewing`  "
cursor.execute(sql)
result = cursor.fetchall()

print("====樹種的資料量====")
print(len(result))

sql = "SELECT DISTINCT `location` FROM `tree_viewing`  "
cursor.execute(sql)
result = cursor.fetchall()

print("====地點的資料量====")
print(len(result))
"""

