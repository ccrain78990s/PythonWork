#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "chen"
"""
109年度餐飲衛生管理分級評核結果 (新竹)
http://127.0.0.1:8888/?action=restaurantall
"""

import json
import sys 
import urllib.request as httplib  # 3.x
import ssl
context = ssl._create_unverified_context()

url="https://odws.hccg.gov.tw/001/Upload/25/opendata/9059/458/0779de36-1aba-42ed-a9ce-1f7426aa639b.json"
req=httplib.Request(url)
try:
    reponse = httplib.urlopen(req, context=context)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents = reponse.read();
        else:
            contents = reponse.read()
        data = json.loads(contents)



        """
        if DataType=="json":
            #JSON
            str1="["
            for x in range(2001,2100):
                str1 = str1+ "{ '地點':'"+data["retVal"][str(x)]["sna"]+"','數量':'"+data["retVal"][str(x)]["tot"]+"'}"  # html
            str1 = str1+"]"
            print(str1)
        else:
             html
        """

        for x in range(0, 96):
            print("食品業者登錄字號:",data[x]["食品業者登錄字號"],"<br>")  # html
            print("店名:", data[x]["店名"], "<br>")
            print("地址:",data[x]["地址"],"電話:",data[x]["電話"] ,"<br>")
            print("緯度:", data[x]["緯度"], "經度:", data[x]["經度"],"<br>")
            print("評核等級:", data[x]["評核等級"],"<br>")
            print("<hr>")

except:                                                                 #  處理網路連線異常
    print("error")   