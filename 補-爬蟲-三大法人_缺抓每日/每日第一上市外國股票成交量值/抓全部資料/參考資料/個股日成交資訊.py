import requests
from bs4 import BeautifulSoup
import os.path
from os import path
import json
import xlrd
import xlwt

target="個股日成交資訊"

# sys.argv
stockID="2330"
# sys.argv
dateTime="20210420"



filename=str(target)+str(dateTime)+'.json'
filenameXls=str(target)+str(dateTime)+'.xls'

if path.exists(filename)==False:    # 是否有  'workfile.txt'檔案
    url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date="+dateTime+"&stockNo="+stockID
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}
    req = requests.get(url, headers=headers)

    print(req.text)
    fr = open(filename, 'w',encoding="UTF-8")
    t1=req.text.encode("UTF-8")
    fr.write(req.text)
    fr.close()

file = open(filename, mode='r',encoding="UTF-8")
json_str = file.read()
file.close()


jsonData = json.loads(json_str)# <---- JSON 字串
#############
fields=jsonData['fields']
print(fields)
t1=jsonData["data"]



#############
# save
write = xlwt.Workbook()             # 新增
write2 = write.add_sheet(str(dateTime)) # 新增'MySheet' 工作表單

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
t1=jsonData["data"]
r=0
for row in t1:    # 每一筆
    print("2330:", row[0], "台積電", row[1])
    c=0
    for col in row:  # 每一個欄位
        value=col
        write2.write(r+1, c, value)  # 寫入value資料 筆數=r, 欄位=c
        c=c+1
    r=r+1

write.save(filenameXls)