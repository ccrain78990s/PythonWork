#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"
"""
臺中市賞樹景點 ↓
https://data.gov.tw/dataset/138706
主要欄位 ↓
項次(臺中市賞樹景點)、縣市別代碼、行政區域代碼、行政區、地點、樹種、花期、備註
"""


import sys
from xml.etree import ElementTree  # XML
import urllib.request as httplib   # Python 3.x 版本寫法

import pymysql as MySQLdb             #  pip install MySQLdb
db = MySQLdb.connect(host="127.0.0.1", user="admin", passwd="admin", db="mydatabase")
cursor = db.cursor()

# 載入檔案方法
#tree = ET.parse('110年臺中市賞樹景點.xml')       #網路上下載來的檔案
#root = tree.getroot()

try:
    #110年臺中市賞樹景點.xml  2021-03-26
    url="https://datacenter.taichung.gov.tw/swagger/OpenData/b9abfa5f-d96c-44b7-9f8f-cf0f39d09002"
    req=httplib.Request(url)
    reponse = httplib.urlopen(req)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            #contents=reponse.read().decode(reponse.headers.get_content_charset())
            contents=reponse.read().decode("UTF-8")
        else:
            contents=reponse.read()

        print(contents)
        root = ElementTree.fromstring(contents)


        print("項次:", root.findall("RECORD/項次")[0].text)
        print("行政區:", root.findall("RECORD/行政區")[0].text)
        print("地點:", root.findall("RECORD/地點")[0].text)
        print("樹種:",root.findall("RECORD/樹種")[0].text)
        print("花期:", root.findall("RECORD/花期")[0].text)
        print(len(root.findall("RECORD")))

        #lst_node = root.findall("RECORD")
        #print(root.findall("MAP/ADDRESS")[0].text)
        #for node in lst_node:
        #    print(node.text)
        x=0
        while x < len(root.findall("RECORD")):
            str1 = "INSERT INTO `tree_viewing`(`id`, `item`, `area`, `location`, `species`, `flowering`)" + \
                   " VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]')"
            str1 = str1.replace("[value-1]", "null")
            str1 = str1.replace("[value-2]", root.findall("RECORD/項次")[x].text)
            str1 = str1.replace("[value-3]", root.findall("RECORD/行政區")[x].text)
            str1 = str1.replace("[value-4]", root.findall("RECORD/地點")[x].text)
            str1 = str1.replace("[value-5]", root.findall("RECORD/樹種")[x].text)
            str1 = str1.replace("[value-6]", root.findall("RECORD/花期")[x].text)
            # print(str1)
            cursor.execute(str1)
            x=x+1
            # print("======資料"++a++"======")
            # print("公園名稱:",data2['pm_name'],"公園介紹:",data2['pm_overview'],"公園地址:",data2['pm_location'],"經度:",data2['pm_lon'],"緯度:",data2['pm_lat'])
        db.commit()
        db.close()

except:
    print("error")
