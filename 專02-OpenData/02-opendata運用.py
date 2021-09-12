#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"

import sys
from xml.etree import ElementTree
import urllib.request as httplib  # 3.x
import matplotlib
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Tkinter 加入 matplotlib圖片
from matplotlib.font_manager import FontProperties  # 中文化
import numpy as np

####
##### OpenData讀取處理
def print_node(node):
    try:
        print("node.text:%s" % node.text)
    except:
        print("node.text:null")


try:
    # 家庭收支調查 - 所得收入者職業別平均每人"所得收入總計" 最後更新時間 2020 - 10 - 27
    url = "https://www.dgbas.gov.tw/public/data/open/localstat/086-%E6%89%80%E5%BE%97%E6%94%B6%E5%85%A5%E8%80%85%E8%81%B7%E6%A5%AD%E5%88%A5%E5%B9%B3%E5%9D%87%E6%AF%8F%E4%BA%BA%E6%89%80%E5%BE%97%E6%94%B6%E5%85%A5%E7%B8%BD%E8%A8%88.xml"
    # 非消費性支出
    #url2=https://www.dgbas.gov.tw/public/data/open/localstat/088-%E6%89%80%E5%BE%97%E6%94%B6%E5%85%A5%E8%80%85%E8%81%B7%E6%A5%AD%E5%88%A5%E5%B9%B3%E5%9D%87%E6%AF%8F%E4%BA%BA%E9%9D%9E%E6%B6%88%E8%B2%BB%E6%94%AF%E5%87%BA.xml
    # 可支配所得
    # url3=https://www.dgbas.gov.tw/public/data/open/localstat/085-%E6%89%80%E5%BE%97%E6%94%B6%E5%85%A5%E8%80%85%E8%81%B7%E6%A5%AD%E5%88%A5%E5%B9%B3%E5%9D%87%E6%AF%8F%E4%BA%BA%E5%8F%AF%E6%94%AF%E9%85%8D%E6%89%80%E5%BE%97.xml
    req = httplib.Request(url)
    reponse = httplib.urlopen(req)
    #req2 = httplib.Request(url2)
    #reponse2 = httplib.urlopen(req2)
    # req3 = httplib.Request(url3)
    # reponse3 = httplib.urlopen(req3)

    if reponse.code == 200:
        if (sys.version_info > (3, 0)):
            # contents=reponse.read().decode(reponse.headers.get_content_charset())
            contents = reponse.read().decode("UTF-8")
            #contents2 = reponse2.read().decode("UTF-8")
            # contents3 = reponse3.read().decode("UTF-8")
        else:
            contents = reponse.read()
            #contents2 = reponse2.read()
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
        #
        listYear=[]
        for x in range(0,len(t0)):
            listYear.append(t1[x].text)

        # 印出所有資料
        for x in range(0, len(t0)):
            print("年份:", t1[x].text)
            print("台灣地區平均每人所得收入總計:", t2[x].text)
            print("   ")
            print("民意代表及主管及經理人員:", t3[x].text)
            print("專業人員:", t4[x].text)
            print("技術員及助理專業人員:", t5[x].text)
            print("事務支援人員:", t6[x].text)
            print("服務及銷售工作人員:", t7[x].text)
            print("農林漁牧業生產人員:", t8[x].text)
            print("技藝有關工作人員:", t9[x].text)
            print("機械設備操作及組裝人員:", t10[x].text)
            print("基層技術工及勞力工:", t11[x].text)
            print("其他:", t12[x].text)
            print("----------------------------")
            print("   ")

        # 定義函數: 每年資料整合成一個list
        def funEveryYearInfo(x):
            list = []
            list.append(int(t3[x].text))
            list.append(int(t4[x].text))
            list.append(int(t5[x].text))
            list.append(int(t6[x].text))
            list.append(int(t7[x].text))
            list.append(int(t8[x].text))
            list.append(int(t9[x].text))
            list.append(int(t10[x].text))
            list.append(int(t11[x].text))
            list.append(int(t12[x].text))
            print(list)
            # 長條圖 : 單獨一年的所得高低
            fig = plt.figure(1, figsize=(20, 4))

            plt.rcParams['font.sans-serif'] = ['SimSun']  # 步驟一（替換sans-serif字型）
            plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）

            labels=['民意代表及主管及經理人員','專業人員','技術員及助理專業人員', '事務支援人員',
                    '服務及銷售工作人員', '農林漁牧業生產人員', '技藝有關工作人員', '機械設備操作及組裝人員', '基層技術工及勞力工', '其他']
            width=0.5
            plt.bar(labels,list,width)
            plt.yticks(np.arange(0,1500000,200000))
            plt.tick_params(axis='x',labelsize=8)   #刻度大小調整
            plt.title(listYear[x]+"年")


            





        # 建立字典 d2={年份:台灣地區所得平均成長率}、d2={年份:民意代表所得平均成長率}...以此類推
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




except:
    print("error")
"""
print(len(t0))
w1=int((int(len(t0)**0.5)+1)*0.5)+1
print(w1)
# funEveryYearInfo(2)
plt.figure('每5年各職業別平均總所得',figsize=(15,10),dpi=100)
y=1
for x in range(0,len(t0),5):
    plt.subplot(w1,w1,y)
    funEveryYearInfo(x)
    y=y+1
plt.tight_layout()
"""

##### 試著讀取、運用OpenData畫圖(matplotlib)

# ↓↓↓ 中文化 ↓↓↓
plt.rcParams['font.sans-serif'] = ['SimSun']  # 步驟一（替換sans-serif字型）
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）


"""
 ↓↓↓ 成長率 折線圖 ↓↓↓
"""

# 補充其他方法 : plt.subplot2grid(shape形狀, location位置, rowspan行跨, colspan列跨)
# 針對台灣地區歷年來平均總所得成長率
plt.figure('歷年來台灣地區各職業別平均總所得成長率',figsize=(10,3),dpi=100)
# Year:台灣地區
plt.subplot(111)   # 1*1的圖片 第1張子圖
names = list(d2.keys())
values = list(d2.values())
plt.plot(names, values, marker='o',color='red')
plt.title('台灣地區平均每人所得總收入成長率')
plt.xticks(rotation=45)

# 歷年來各職業別平均總所得成長率
plt.figure('歷年來各職業別平均總所得成長率',figsize=(15,12),dpi=100)
# Year:民意代表及主管及經理人員
plt.subplot(521)
names = list(d3.keys())
values = list(d3.values())
plt.plot(names, values, marker='o')
plt.title('民意代表及主管及經理人員')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)

# Year:專業人員
plt.subplot(522)
names = list(d4.keys())
values = list(d4.values())
plt.plot(names, values, marker='o')
plt.title('專業人員')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)
# Year:技術員及助理專業人員
plt.subplot(523)
names = list(d5.keys())
values = list(d5.values())
plt.plot(names, values, marker='o')
plt.title('技術員及助理專業人員')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)
# Year:事務支援人員
plt.subplot(524)
names = list(d6.keys())
values = list(d6.values())
plt.plot(names, values, marker='o')
plt.title('事務支援人員')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)
# Year:服務及銷售工作人員
plt.subplot(525)
names = list(d7.keys())
values = list(d7.values())
plt.plot(names, values, marker='o')
plt.title('服務及銷售工作人員')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)
# Year:農林漁牧業生產人員
plt.subplot(526)
names = list(d8.keys())
values = list(d8.values())
plt.plot(names, values, marker='o')
plt.title('農林漁牧業生產人員')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)
# Year:技藝有關工作人員
plt.subplot(527)
names = list(d9.keys())
values = list(d9.values())
plt.plot(names, values, marker='o')
plt.title('技藝有關工作人員')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)
# Year:機械設備操作及組裝人員
plt.subplot(528)
names = list(d10.keys())
values = list(d10.values())
plt.plot(names, values, marker='o')
plt.title('機械設備操作及組裝人員')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)
# Year:基層技術工及勞力工
plt.subplot(529)
names = list(d11.keys())
values = list(d11.values())
plt.plot(names, values, marker='o')
plt.title('基層技術工及勞力工')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)
# Year:其他
plt.subplot(5,2,10)
names = list(d12.keys())
values = list(d12.values())
plt.plot(names, values, marker='o')
plt.title('其他')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)

plt.tight_layout()  # 間距調整 設定留白
plt.show()


"""
###### 運用matplotlib把圖顯示在Tkinter上-測試用
root = tk.Tk()
root.title("專案練習 - matplotlib in TK")

matplotlib.use('TkAgg')
# Initialize matplotlib figure for graphing purposes
fig = plt.figure(1,figsize=(9,3))

# Special type of "canvas" to allow for matplotlib graphing
canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()
names = list(d2.keys())
values = list(d2.values())
plt.plot(names, values, marker='o')
plt.title('台灣地區平均每人所得總收入成長率')
plot_widget.grid(row=0, column=0)

root.mainloop()


"""

"""
root = tk.Tk()
root.title("專案練習 - matplotlib in TK")

root.minsize(width=380, height=400)                      #視窗最小尺寸
root.maxsize(width=3000, height=3000)                      #視窗最大尺寸
root.resizable(width=True, height=True)                #是否可調整視窗大小



matplotlib.use('TkAgg')
# Initialize matplotlib figure for graphing purposes
fig1 = plt.figure(1,figsize=(20,3))

# Special type of "canvas" to allow for matplotlib graphing
canvas = FigureCanvasTkAgg(fig1, master=root)
plot_widget = canvas.get_tk_widget()

plt.subplot(111)    # 3*1的圖片 第1張子圖
names = list(d2.keys())
values = list(d2.values())
plt.plot(names, values, marker='o')
plt.title('台灣地區平均每人所得總收入成長率')
plt.xticks(rotation=45)

plot_widget.grid(row=0, column=0)

fig2=plt.figure(2,figsize=(20,6))
canvas = FigureCanvasTkAgg(fig2, master=root)
plot_widget = canvas.get_tk_widget()

plt.subplot(431)
names = list(d3.keys())
values = list(d3.values())
plt.plot(names, values, marker='o')
plt.title('民意代表及主管及經理人員')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)
# Year:專業人員
plt.subplot(432)
names = list(d4.keys())
values = list(d4.values())
plt.plot(names, values, marker='o')
plt.title('專業人員')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)
# Year:技術員及助理專業人員
plt.subplot(433)
names = list(d5.keys())
values = list(d5.values())
plt.plot(names, values, marker='o')
plt.title('技術員及助理專業人員')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)
# Year:事務支援人員
plt.subplot(434)
names = list(d6.keys())
values = list(d6.values())
plt.plot(names, values, marker='o')
plt.title('事務支援人員')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)
# Year:服務及銷售工作人員
plt.subplot(435)
names = list(d7.keys())
values = list(d7.values())
plt.plot(names, values, marker='o')
plt.title('服務及銷售工作人員')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)
# Year:農林漁牧業生產人員
plt.subplot(436)
names = list(d8.keys())
values = list(d8.values())
plt.plot(names, values, marker='o')
plt.title('農林漁牧業生產人員')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)
# Year:技藝有關工作人員
plt.subplot(437)
names = list(d9.keys())
values = list(d9.values())
plt.plot(names, values, marker='o')
plt.title('技藝有關工作人員')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)
# Year:機械設備操作及組裝人員
plt.subplot(438)
names = list(d10.keys())
values = list(d10.values())
plt.plot(names, values, marker='o')
plt.title('機械設備操作及組裝人員')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)
# Year:基層技術工及勞力工
plt.subplot(439)
names = list(d11.keys())
values = list(d11.values())
plt.plot(names, values, marker='o')
plt.title('基層技術工及勞力工')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)
# Year:其他
plt.subplot(4,3,10)
names = list(d12.keys())
values = list(d12.values())
plt.plot(names, values, marker='o')
plt.title('其他')
plt.xticks(rotation=45)
plt.tick_params(axis='x',labelsize=8)

plt.tight_layout()  # 間距調整 設定留白

plot_widget.grid(row=1, column=0)

root.mainloop()

"""
