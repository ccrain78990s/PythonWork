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

rate="民意代表及主管及經理人員"
if len(sys.argv)>1:
    rate=sys.argv[1]

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

        # 建立字典 d2={年份:台灣地區所得平均成長率}、d3={年份:民意代表所得平均成長率}...以此類推
        d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
        for z in range(1, len(t0)):
            d2[t1[z].text] = (int(t2[z].text) - int(t2[z - 1].text)) / int(t2[z - 1].text)
            d3[t1[z].text] = (int(t3[z].text) - int(t3[z - 1].text)) / int(t3[z - 1].text)
            d4[t1[z].text] = (int(t4[z].text) - int(t4[z - 1].text)) / int(t4[z - 1].text)
            d5[t1[z].text] = (int(t5[z].text) - int(t5[z - 1].text)) / int(t5[z - 1].text)
            d6[t1[z].text] = (int(t6[z].text) - int(t6[z - 1].text)) / int(t6[z - 1].text)
            d7[t1[z].text] = (int(t7[z].text) - int(t7[z - 1].text)) / int(t7[z - 1].text)
            d8[t1[z].text] = (int(t8[z].text) - int(t8[z - 1].text)) / int(t8[z - 1].text)
            d9[t1[z].text] = (int(t9[z].text) - int(t9[z - 1].text)) / int(t9[z - 1].text)
            d10[t1[z].text] = (int(t10[z].text) - int(t10[z - 1].text)) / int(t10[z - 1].text)
            d11[t1[z].text] = (int(t11[z].text) - int(t11[z - 1].text)) / int(t11[z - 1].text)
            d12[t1[z].text] = (int(t12[z].text) - int(t12[z - 1].text)) / int(t12[z - 1].text)


        if rate == "臺灣地區":
            for year in d2:
                rate_=d2[year]
                print('%s 年成長率= %s' % (year,rate_),"</br>")
        elif rate== "民意代表及主管及經理人員":
            for year in d3:
                rate_=d3[year]
                print('%s 年成長率= %s' % (year,rate_),"</br>")
        elif rate== "專業人員":
            for year in d4:
                rate_=d4[year]
                print('%s 年成長率= %s' % (year,rate_),"</br>")
        elif rate== "技術員及助理專業人員":
            for year in d5:
                rate_=d5[year]
                print('%s 年成長率= %s' % (year,rate_),"</br>")
        elif rate== "事務支援人員":
            for year in d6:
                rate_=d6[year]
                print('%s 年成長率= %s' % (year,rate_),"</br>")
        elif rate== "服務及銷售工作人員":
            for year in d7:
                rate_=d7[year]
                print('%s 年成長率= %s' % (year,rate_),"</br>")
        elif rate== "農林漁牧業生產人員":
            for year in d8:
                rate_=d8[year]
                print('%s 年成長率= %s' % (year,rate_),"</br>")
        elif rate== "技藝有關工作人員":
            for year in d9:
                rate_=d9[year]
                print('%s 年成長率= %s' % (year,rate_),"</br>")
        elif rate== "機械設備操作及組裝人員":
            for year in d10:
                rate_=d10[year]
                print('%s 年成長率= %s' % (year,rate_),"</br>")
        elif rate== "基層技術工及勞力工":
            for year in d11:
                rate_=d11[year]
                print('%s 年成長率= %s' % (year,rate_),"</br>")
        elif rate== "其他":
            for year in d12:
                rate_=d12[year]
                print('%s 年成長率= %s' % (year,rate_),"</br>")


except:                                                                 #  處理網路連線異常
    print("error")   