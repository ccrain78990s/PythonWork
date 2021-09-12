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
add="三民蝙蝠洞"
if len(sys.argv)>1:
    add=sys.argv[1]



context = ssl._create_unverified_context()
url="https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=rdec-key-123-45678-011121314"
req=httplib.Request(url)
try:
        reponse = httplib.urlopen(req, context=context)
        if reponse.code == 200:
            contents = reponse.read() #.decode("UTF-8")
            # print(contents)
            data = json.loads(contents)

            for x in range(0,len(data['infos'])):
                if add in data['infos'][x]['Add']:
                    print("====", data['infos'][x]['Name'], "====")
                    print("地址", data['infos'][x]['Add'])
                    print("停車資訊", data['infos'][x]['Parkinginfo'])
                    print("門票費用", data['infos'][x]['Ticketinfo'])

except:                                         #  處理網路連線異常
        print("error")

