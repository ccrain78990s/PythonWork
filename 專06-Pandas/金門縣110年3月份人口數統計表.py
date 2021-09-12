#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "Chen"

"""
資料來源:
金門縣110年3月份人口數統計表
https://data.gov.tw/dataset/138931

主要欄位說明:
編號、村里數、鄰數、戶數、男數、女數、總人口數、出生人數、死亡人數、結婚對數、離婚對數、遷入人數、遷出人數
"""

import pandas as pd
import matplotlib.pyplot as plt
# 圖表顯示中文文字
from matplotlib.font_manager import FontProperties  # 中文化
plt.rcParams['font.sans-serif'] = ['SimSun']  # 步驟一（替換sans-serif字型）
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）


df = pd.read_json('https://ws.kinmen.gov.tw/001/Upload/0/relfile/0/0/833d2f82-2ae1-49c9-957a-707f28c8225e.json')

print(df.head(5))   # 前面五筆資料
print(type(df))
# 2 data info
print(df.shape)
print(df.columns)
print(df.index)
print(df.info())
print(df.describe())
print(df)   # 資料列印














