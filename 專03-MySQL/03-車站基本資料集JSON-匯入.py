#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"
import json
import sys
try:
    import urllib2 as httplib   # 2.x
except Exception:
    import urllib.request as httplib  # 3.x
    import ssl
    import urllib.request

try:
 import MySQLdb                         # pip install MySQL-python
except:
 import pymysql as MySQLdb             #  pip install MySQLdb
db = MySQLdb.connect(host="127.0.0.1", user="admin", passwd="admin", db="mydatabase")
cursor = db.cursor()

#import matplotlib.pyplot as plt

"""
資料來源:
台鐵車站基本資料
https://data.gov.tw/dataset/33425
JSON=https://quality.data.gov.tw/dq_download_json.php?nid=33425&md5_url=82a54f59aa0559d7c4ef0aadb1ec1510

stationCode(車站代碼)、
stationName(中文站名)、stationEName(英文站名)、
name(網站中文站名)、ename(網站英文站名)、
stationAddrTw(車站地址)、stationAddrEn(車站英文地址)、
stationTel(車站電話)、gps

"""

url="https://quality.data.gov.tw/dq_download_json.php?nid=33425&md5_url=82a54f59aa0559d7c4ef0aadb1ec1510"

req=httplib.Request(url)
try:
    context = ssl._create_unverified_context()  #<----
    reponse = httplib.urlopen(url, context=context)  #<----
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
                #contents=reponse.read().decode(reponse.headers.get_content_charset())
                contents=reponse.read().decode("utf-8")
                #print(contents)
                #contents=contents.replace("\r\n", "")
                #print(contents)
        else:
                contents=reponse.read()
        data = json.loads(contents)
        print("車站代碼:",data[0]["stationCode"])
        print("站名:",data[0]["stationName"])
        print("地址:", data[0]["stationAddrTw"])
        print("電話:", data[0]["stationTel"])
        print("GPS經緯度:", data[0]["gps"])
        print(len(data))

        for data2 in data:
            str1 = "INSERT INTO `station_info`(`id`, `stationCode`, `stationName`, `stationAddrTw`, `stationTel`, `gps`)" + \
                   " VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]')"
            str1 = str1.replace("[value-1]", "null")
            str1 = str1.replace("[value-2]", str(data2["stationCode"]))
            str1 = str1.replace("[value-3]", str(data2["stationName"]))
            str1 = str1.replace("[value-4]", str(data2["stationAddrTw"]))
            str1 = str1.replace("[value-5]", str(data2["stationTel"]))
            str1 = str1.replace("[value-6]", str(data2["gps"]))
            #print(str1)
            cursor.execute(str1)
            #print("======資料"++a++"======")
            # print("公園名稱:",data2['pm_name'],"公園介紹:",data2['pm_overview'],"公園地址:",data2['pm_location'],"經度:",data2['pm_lon'],"緯度:",data2['pm_lat'])
        db.commit()
        db.close()




except:     #  處理網路連線異常
    print("error")






