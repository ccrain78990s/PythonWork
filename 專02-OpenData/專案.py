#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"

import sys
from xml.etree import ElementTree
import urllib.request as httplib  # 3.x
import matplotlib.pyplot as plt
# 中文化
from matplotlib.font_manager import FontProperties  # 步驟一

def print_node(node):
    try:
       print("node.text:%s" % node.text)
    except:
       print("node.text:null")


try:
    #家庭收支調查 - 所得收入者職業別平均每人"所得收入總計" 最後更新時間 2020 - 10 - 27
    url="https://www.dgbas.gov.tw/public/data/open/localstat/086-%E6%89%80%E5%BE%97%E6%94%B6%E5%85%A5%E8%80%85%E8%81%B7%E6%A5%AD%E5%88%A5%E5%B9%B3%E5%9D%87%E6%AF%8F%E4%BA%BA%E6%89%80%E5%BE%97%E6%94%B6%E5%85%A5%E7%B8%BD%E8%A8%88.xml"
    #非消費性支出
    #url2=https://www.dgbas.gov.tw/public/data/open/localstat/088-%E6%89%80%E5%BE%97%E6%94%B6%E5%85%A5%E8%80%85%E8%81%B7%E6%A5%AD%E5%88%A5%E5%B9%B3%E5%9D%87%E6%AF%8F%E4%BA%BA%E9%9D%9E%E6%B6%88%E8%B2%BB%E6%94%AF%E5%87%BA.xml
    #可支配所得
    #url3=https://www.dgbas.gov.tw/public/data/open/localstat/085-%E6%89%80%E5%BE%97%E6%94%B6%E5%85%A5%E8%80%85%E8%81%B7%E6%A5%AD%E5%88%A5%E5%B9%B3%E5%9D%87%E6%AF%8F%E4%BA%BA%E5%8F%AF%E6%94%AF%E9%85%8D%E6%89%80%E5%BE%97.xml
    req=httplib.Request(url)
    reponse = httplib.urlopen(req)
    #req2 = httplib.Request(url2)
    #reponse2 = httplib.urlopen(req2)
    #req3 = httplib.Request(url3)
    #reponse3 = httplib.urlopen(req3)

    if reponse.code==200:
        if (sys.version_info > (3, 0)):
            #contents=reponse.read().decode(reponse.headers.get_content_charset())
            contents=reponse.read().decode("UTF-8")
            #contents2 = reponse2.read().decode("UTF-8")
            #contents3 = reponse3.read().decode("UTF-8")
        else:
            contents=reponse.read()
            # contents2 = reponse2.read()
            # contents3 = reponse3.read()

        """
        fr = open('workfile.txt', 'w')
        fr.write(contents)
        fr.close()
        """


        print(contents)
        print_node(contents)
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

        for x in range(0,len(t0)):
            print("年份:",t1[x].text)
            print("台灣地區平均每人所得收入總計:",t2[x].text)
            print("   ")
            print("民意代表及主管及經理人員:",t3[x].text)
            print("專業人員:",t4[x].text)
            print("技術員及助理專業人員:",t5[x].text)
            print("事務支援人員:",t6[x].text)
            print("服務及銷售工作人員:",t7[x].text)
            print("農林漁牧業生產人員:",t8[x].text)
            print("技藝有關工作人員:",t9[x].text)
            print("機械設備操作及組裝人員:",t10[x].text)
            print("基層技術工及勞力工:",t11[x].text)
            print("其他:",t12[x].text)
            print("----------------------------")
            print("   ")
            #print_node(node)



        """
        圓餅圖試畫:
        def fun1(x):
            #中文化 ↓
            plt.rcParams['font.sans-serif'] = ['SimSun']  # 步驟一（替換sans-serif字型）
            plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）

            t13 = float(t3[x].text)+float(t4[x].text)+float(t5[x].text)\
                  +float(t6[x].text)+float(t7[x].text)+float(t8[x].text)\
                  +float(t9[x].text)+float(t10[x].text)+float(t11[x].text)\
                  +float(t12[x].text)

            t14 = float(t3[x].text) / t13
            t15 = float(t4[x].text) / t13
            t16 = float(t5[x].text) / t13
            t17 = float(t6[x].text) / t13
            t18 = float(t7[x].text) / t13
            t19 = float(t8[x].text) / t13
            t20 = float(t9[x].text) / t13
            t21 = float(t10[x].text) / t13
            t22 = float(t11[x].text) / t13
            t23 = float(t12[x].text) / t13

            labels = '民意代表及主管及經理人員', '專業人員', '技術員及助理專業人員',\
            '事務支援人員', '服務及銷售工作人員', '農林漁牧業生產人員',\
            '技藝有關工作人員', '機械設備操作及組裝人員', '基層技術工及勞力工',\
            '其他'

            sizes = [t14, t15, t16, t17, t18, t19, t20, t21, t22, t23]
            explode = (0.1, 0.1, 0.1, 0.1, 0.1,
                       0.1, 0.1, 0.1, 0.1, 0.1)

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            plt.show()


        fun1(1)
        """

except:
    print("error")
#畫圖
# ↓↓↓ 中文化
plt.rcParams['font.sans-serif'] = ['SimSun']  # 步驟一（替換sans-serif字型）
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）


plt.subplot(2, 1, 1)
# Year:台灣地區
d = {}
for z in range(1, len(t0)):
    d[t1[z].text] = (int(t2[z].text)-int(t2[z-1].text))/int(t2[z-1].text)

names = list(d.keys())
values = list(d.values())

plt.plot(names, values,marker='o')
plt.suptitle('台灣地區平均每人所得總收入成長率')




plt.subplot(2, 2, 3)
# Year:民意代表及主管及經理人員
d2 = {}
for z in range(1, len(t0)):
    d2[t1[z].text] = (int(t3[z].text)-int(t3[z-1].text))/int(t3[z-1].text)

names = list(d2.keys())
values = list(d2.values())

plt.plot(names, values,marker='o')
plt.suptitle('民意代表及主管及經理人員平均每人所得總收入成長率')


plt.tight_layout()          #間距調整
plt.show()

#Plotting categorical variables類別變數
"""
#1
import matplotlib.pyplot as plt

data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Categorical Plotting')
#2
cat = ["bored", "happy", "bored", "bored", "happy", "bored"]
dog = ["happy", "happy", "happy", "happy", "bored", "bored"]
activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]

fig, ax = plt.subplots()
ax.plot(activity, dog, label="dog")
ax.plot(activity, cat, label="cat")
ax.legend()

plt.show()
"""

#GUI


