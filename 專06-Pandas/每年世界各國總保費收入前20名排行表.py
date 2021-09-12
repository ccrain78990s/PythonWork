#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"

"""
資料來源:
世界各國總保費收入前20名排行表
https://data.gov.tw/dataset/129377

主要欄位說明:
年月、洲別、國家、排名總計、保費收入總計_百萬美元、占有率總計、
財產保險業排名、財產保險業保費收入_百萬美元、財產保險業占有率、
人身保險業排名、人身保險業保費收入_百萬美元、人身保險業占有率、
公告日期
"""

import pandas as pd
import matplotlib.pyplot as plt
# 圖表顯示中文文字
from matplotlib.font_manager import FontProperties  # 中文化
plt.rcParams['font.sans-serif'] = ['SimSun']  # 步驟一（替換sans-serif字型）
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）


df = pd.read_csv('每年世界各國總保費收入前20名排行表.csv')

print(df.head(5))   # 前面五筆資料
print(type(df))
# 2 data info
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())
print(df)   # 資料列印

print(df.sort_values(by=['排名總計']))
#2019總排名
df2019=df[df.年月==2019]
df2019=df2019[['年月','洲別','國家','排名總計','保費收入總計_百萬美元','占有率總計']]
print(df2019.sort_values(by=['排名總計']))

df2019.plot(x='國家',y='保費收入總計_百萬美元',kind='bar')
plt.title('2019年前20名國保費收入總計(百萬美元)')
plt.show()


#2018總排名
#2017總排名
#財產保險
#人身保險

"""
# 第二題: 把 [年月,上市家數,上市資本額_十億元]  印出來
print(df[["年月","上市家數","上市資本額_十億元"]])
# 第三題: 找出 2019 年的資料          # if
print(df[df['年月'] >= 201901])  # int64
# print(df[(df['Date'] >= '2018-07-05') & (df['Date'] <= '2018-07-10' )])
#202001
# 第四題: 找出 上市成長率  最高的年月   # if
print("第四題: 找出 上市成長率  最高的年月----------")
#print(df["營業收入"].max())
#t1=df["營業收入"].idxmax()
#print("營業收入id:",t1)
#print(df.iloc[t1])
# 第五題: 找出 2019 年的[上市成長率] 最高的月份
# 第六題: 找出 2018 年的資料
# 第七題: 比較 2017  和 2018 年的[上市資本額_十億元]  情況 (差異)

print(df.head(5))   # 前面五筆資料
df=df.set_index('年月')
print(df.head(5))   # 前面五筆資料
dfA=df[1:5]
dfB=df[5:10]
dfC=dfA-dfB
print(dfC)
exit()   # 離開











print(df['公司代號'])
print(df[['公司代號','公司名稱']])

# 1. 全部的公司代號
#.2.

# 3.
# 1101	到 1110  所有資料
# solution 1
t1=df[["公司代號","公司名稱"]]
print(t1[0:7])

# solution 2
print(df[["公司代號","公司名稱"]][0:7])

# solution 3
print(df[["公司代號","公司名稱"]].values[0:7])   # List
print(df[["公司代號","公司名稱"]].iloc[0:7])



print(df[0:7])

# 營業收入
# [營業收入] 最大的上市公司
# [營業利益] 最大的上市公司


print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())

print(df["營業收入"].shape)
print(df["營業收入"].index)
print(df["營業收入"].describe())

print(df[["公司名稱","營業收入"]].shape)
print(df["營業收入"].max())

print("營業收入----------")
print(df["營業收入"].max())
t1=df["營業收入"].idxmax()
print("營業收入id:",t1)
print(df.iloc[t1])

print("營業收入 min ----------")
print(df["營業收入"].min())
t1=df["營業收入"].idxmin()
print("營業收入id:",t1)
print(df.iloc[t1])


import numpy as np
df['營業利益'] = df['營業利益'].replace(np.nan, 0)   # nan null
df['營業利益'] = df['營業利益'].replace("--", 0)     # -- 換成 0
#df["營業利益"] = df["營業利益"].astype(str)               #  int 轉   字串
df["營業利益"] = df["營業利益"].astype(np.int64)       #  字串轉 int
#df["營業利益"] = pd.to_numeric(df["營業利益"])       #  字串轉 int


print("營業利益----------")
print(df["營業利益"].max())
t1=df["營業利益"].idxmax()
print("營業利益:",t1)
print(df.iloc[t1])


print("營業利益 min ----------")
print(df["營業利益"].min())
t1=df["營業利益"].idxmin()
print("營業利益:",t1)
print(df.iloc[t1])


#. 基本每股盈餘(元)   Top 10
# Close 價格最高的 Top 5
print("---------基本每股盈餘(元)   Top 10")
t2=df.sort_values(by=['基本每股盈餘(元)'], ascending=False)          # 依照Close 數字大的排列
t3=t2[:10]                                                 # 依照Close數字最大的 5 筆
print(t3)

# 營業收入	top 10
print("---------營業收入   Top 10")
t2=df.sort_values(by=['營業收入'], ascending=False)          # 依照 [營業收入] 數字大的排列
t3=t2[:10]                                                 # 依照 [營業收入] 數字最大的 5 筆
print(t3)

# 營業利益	top 10
# 營業外收入及支出 top 10
# 基本每股盈餘(元) top 10

# 營業外收入及支出  >  營業收入  top 10

print("---------營業外收入及支出  >  營業收入    Top 10")
df["營業外減業內"]=df["營業外收入及支出"]-df["營業收入"]
t2=df.sort_values(by=['營業外減業內'], ascending=False)          # 依照 [營業外減業內]  數字大的排列
t3=t2[:10]                                                 # 依照 [營業外減業內] 數字最大的 5 筆
print(t3)


df["營業外收入及支出>營業收入"]=df["營業外收入及支出"]-df["營業收入"]
t2=df.sort_values(by=['營業外收入及支出>營業收入'], ascending=False)          # 依照 [營業外收入及支出>營業收入]  數字大的排列
t3=t2[:10]                                                 # 依照[營業外收入及支出>營業收入]數字最大的 5 筆
print(t3)
"""







