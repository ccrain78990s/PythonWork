# import requests
from bs4 import BeautifulSoup
import os.path
from os import path
import urllib.request as httplib  # 3.x
import json
# save
import xlrd
import xlwt


target="每日第一上市外國股票收盤行情"
date=20210416


filename=str(date)+str(target)+'.jason'
url = "https://www.twse.com.tw/exchangeReport/STOCK_FIRST?response=json&date="+str(date)+"&_=1618559415314"
if path.exists(filename)==False:    # 是否有  'workfile.txt'檔案

    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}
    # req = requests.get(url, headers=headers)
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    req=httplib.Request(url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
    })
    reponse = httplib.urlopen(req)
    if reponse.code==200:
        contents = reponse.read().decode(reponse.headers.get_content_charset())
        # contents = reponse.read().decode("utf-8")
        # contents = reponse.read()
        print(contents)
        fr = open(filename, 'w',encoding="UTF-8")
        fr.write(contents)
        fr.close()

with open(filename, mode='r',encoding="UTF-8") as f:
    # str1=f.read()
    data = json.load(f)
    
#print(data)
#print(data['title'])
#print(data['data'])

for x in data['data']:
    print("證券代號",x[0],"證券名稱", x[1])
    print("成交股數", x[2],"成交筆數",x[3],"成交金額",x[4])
    print("開盤價", x[5], "最高價", x[6], "最低價", x[7], "收盤價", x[8])
    x[9]=x[9].replace("<span style='color:green'>","")
    x[9] = x[9].replace("<span style='color:red'>", "")
    x[9]=x[9].replace("</sapn>","")
    print("+/-", x[9], "漲跌價", x[10])
    print("最後揭示買價", x[11], "買進揭示委託數量", x[12], "最後揭示賣價", x[13], "賣出揭示委託數量", x[14])
    print("本益比", x[15])
    print(" ")




###############
# save
fields=data['fields']
filenameXls=str(date)+str(target)+'.xls'

write = xlwt.Workbook()             # 新增
write2 = write.add_sheet(str(date)) # 新增'MySheet' 工作表單

#欄位
for i in range(len(fields)):  # 數字
    value =fields[i]
    write2.write(0, i, value)  # 寫入value資料 筆數=0, 欄位=i

# 資料

"""  版本一 while
t1=jsonData["data"]
row=0
while row<len(t1):    # 每一筆
    print("id:", t1[row][0], "公司名稱", t1[row][1])
    col=0
    while col<len(t1[row]):  # 每一個欄位
        value=t1[row][col]
        write2.write(row+1, col, value)  # 寫入value資料 筆數=row, 欄位=col
        col=col+1
    row=row+1
"""
t1=data["data"]
r=0
for row in t1:    # 每一筆
    print("id:", row[0], "公司名稱", row[1])
    c=0
    for col in row:  # 每一個欄位
        value=col
        write2.write(r+1, c, value)  # 寫入value資料 筆數=r, 欄位=c
        c=c+1
    r=r+1

write.save(filenameXls)             # save

