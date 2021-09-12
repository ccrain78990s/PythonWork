#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"
"""
家庭收支調查 - 所得收入者【職業別】平均每人【所得收入】總計
"""
import sys
import urllib.request as httplib  # 3.x
from xml.etree import ElementTree
import ssl

context = ssl._create_unverified_context()

try:
    # 家庭收支調查 - 所得收入者職業別平均每人"所得收入總計" 最後更新時間 2020 - 10 - 27
    url = "https://www.dgbas.gov.tw/public/data/open/localstat/086-%E6%89%80%E5%BE%97%E6%94%B6%E5%85%A5%E8%80%85%E8%81%B7%E6%A5%AD%E5%88%A5%E5%B9%B3%E5%9D%87%E6%AF%8F%E4%BA%BA%E6%89%80%E5%BE%97%E6%94%B6%E5%85%A5%E7%B8%BD%E8%A8%88.xml"
    req = httplib.Request(url)
    reponse = httplib.urlopen(req)


    if reponse.code == 200:
        if (sys.version_info > (3, 0)):
            contents = reponse.read().decode("UTF-8")

        else:
            contents = reponse.read()




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
        #
        listYear = []
        for x in range(0, len(t0)):
            listYear.append(t1[x].text)



        if rate == '':
            print("地點:", data["retVal"][str(x)]["sna"], " 數量:", data["retVal"][str(x)]["tot"], " 區:",
                  data["retVal"][str(x)]["sarea"], "<br>")  # html

"""
DataType="json"
sarea="中壢區"
# print(len(sys.argv))
if len(sys.argv)>1:
    sarea=sys.argv[1]
if len(sys.argv)>2:
    DataType=sys.argv[2]
"""




except:                                                                 #  處理網路連線異常
    print("error")   