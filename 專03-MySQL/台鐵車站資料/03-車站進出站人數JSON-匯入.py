#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"
import json
import sys
import urllib.request as httplib  # 3.x
import ssl

import pymysql as MySQLdb             #  pip install MySQLdb
db = MySQLdb.connect(host="127.0.0.1", user="admin", passwd="admin", db="mydatabase")
cursor = db.cursor()

"""
資料來源:
每日各站點進出站人數(2019.04.23~)
https://data.gov.tw/dataset/8792


trnOpDate(乘車日)、staCode(車站代碼)、gateInComingCnt(進站人數)、gateOutGoingCnt(出站人數)
"""

url="https://quality.data.gov.tw/dq_download_json.php?nid=8792&md5_url=dd6c0bd09f95d4774adc44310f059b13"
req=httplib.Request(url)
try:
    context = ssl._create_unverified_context()  #<----
    reponse = httplib.urlopen(url, context=context)  #<----
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
                #contents=reponse.read().decode(reponse.headers.get_content_charset())
                contents=reponse.read().decode("utf-8")
                #print(contents)

        else:
                contents=reponse.read()
        data = json.loads(contents)
        print("乘車日:",data[0]["trnOpDate"])
        print("車站代碼:",data[0]["staCode"])
        print("進站人數:", data[0]["gateInComingCnt"])
        print("出站人數:", data[0]["gateOutGoingCnt"])
        print("====資料量====")
        print(len(data))
        """
        for x in range(0,len(data)):
            print("乘車日:", data[x]["trnOpDate"])
            print("車站代碼:", data[x]["staCode"])
            print("進站人數:", data[x]["gateInComingCnt"])
            print("出站人數:", data[x]["gateOutGoingCnt"])
        """
        """
        for data2 in data:
            str1 = "INSERT INTO `station_in_and_out`(`id`, `trnOpDate`, `staCode`, `gateInComingCnt`, `gateOutGoingCnt`)" + \
                   " VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]')"
            str1 = str1.replace("[value-1]", "null")
            str1 = str1.replace("[value-2]", data2["trnOpDate"])
            str1 = str1.replace("[value-3]", str(data2["staCode"]))
            str1 = str1.replace("[value-4]", data2["gateInComingCnt"])
            str1 = str1.replace("[value-5]", data2["gateOutGoingCnt"])

            #print(str1)
            cursor.execute(str1)
            
        db.commit()
        db.close()
        """



except:     #  處理網路連線異常
    print("error")






