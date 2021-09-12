#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"
"""
桃園市住宿資料(中)
InfoId(序號)、TYWebsite(導覽網網址)、Name(名稱)、Toldescribe(簡述)、Add(地址)、Zipcode(郵遞區號)、
Opentime(開放時間)、Px(X座標)、Py(Y座標)、Website(網站)、Parkinginfo(停車資訊)、Remarks(旅遊叮嚀)、
Tel(電話)、Fax(傳真)、Changetime(更新時間)、Charge(更新時間)
"""

import json
import sys
import urllib.request as httplib  # 3.x

DataType=""
sarea="中壢區"
# print(len(sys.argv))
if len(sys.argv)>1:
    sarea=sys.argv[1]
if len(sys.argv)>2:
    DataType=sys.argv[2]



import ssl
context = ssl._create_unverified_context()

url="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=908d67d9-eb77-4f17-88c2-068b2dd74d27&rid=c3340a19-9219-498a-9a46-21de506ba85b"
req=httplib.Request(url)
try:
    reponse = httplib.urlopen(req, context=context)
    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            contents = reponse.read();
        else:
            contents = reponse.read()
        data = json.loads(contents)
        #html
        print(data['infos'][0])
        print(len(data['infos']))
        print("====",data['infos'][0]['Name'],"====")
        print("導覽網址",data['infos'][0]['TYWebsite'])
        print("地址",data['infos'][0]['Add'])
        print("營業時間",data['infos'][0]['Opentime'])
        print("停車資訊",data['infos'][0]['Parkinginfo'])
        print("電話",data['infos'][0]['Tel'])
        #
        for x in range(0,len(data['infos'])):
            if "蘆竹區" in data['infos'][x]['Add']:
                print("====", data['infos'][x]['Name'], "====")
                print("導覽網址", data['infos'][x]['TYWebsite'])
                print("地址", data['infos'][x]['Add'])
                print("營業時間", data['infos'][x]['Opentime'])
                print("停車資訊", data['infos'][x]['Parkinginfo'])
                print("電話", data['infos'][x]['Tel'])
            #else:
            #    print("查無您所輸入的相關資料，請檢查是否有打錯字或是更換搜尋訊息")
        """
        DataType = ""
        if DataType=="json":
            #JSON
            str1="["
            for x in range(2001,2100):
                str1 = str1+ "{ '地點':'"+data["retVal"][str(x)]["sna"]+"','數量':'"+data["retVal"][str(x)]["tot"]+"'}"  # html
            str1 = str1+"]"
            print(str1)
        else:
            # html
            for x in range(2001, 2100):
                if sarea == data["retVal"][str(x)]["sarea"]:
                    print("地點:", data["retVal"][str(x)]["sna"], " 數量:", data["retVal"][str(x)]["tot"], " 區:",
                          data["retVal"][str(x)]["sarea"], "<br>")  # html
        """

except:                                                                 #  處理網路連線異常
    print("error")   