#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"

import json
import sys 
import urllib.request as httplib  # 3.x
import ssl
import sys
from datetime import datetime
# python 08-WeatherData.py "臺北市"
#print("Arguments count:",len(sys.argv))
city="臺北市"
if len(sys.argv)>1:
    city=sys.argv[1]
print(city)


context = ssl._create_unverified_context()
url="https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=5ca2bfc7-9ace-4719-88ae-4034b9a5a55c&rid=a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f"
url="https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=rdec-key-123-45678-011121314"
req=httplib.Request(url)
try:
        reponse = httplib.urlopen(req, context=context)
        if reponse.code == 200:
            contents = reponse.read() #.decode("UTF-8")
            # print(contents)
            data = json.loads(contents)
            t1 = data["records"]["location"]
            for data2 in t1:
                if city == data2["locationName"]:
                    print(data2["weatherElement"][0]["time"][0]["parameter"]["parameterName"])

            if(len(data)>1):                        # 確認是否有資料
                now = datetime.now()  # 現在時間
                current_time = now.strftime("%Y%m%d%H%M%S")  # 印出時間的格式
                #print("現在時間 =", current_time)
                with open('c:\\天氣'+str(current_time)+'.json', 'w') as f:   # 處存
                    json.dump(data, f)
except:                                         #  處理網路連線異常
        print("error")

