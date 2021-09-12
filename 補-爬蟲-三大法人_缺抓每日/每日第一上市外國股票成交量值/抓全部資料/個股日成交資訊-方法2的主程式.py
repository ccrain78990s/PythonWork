import requests
from bs4 import BeautifulSoup
import os.path
from os import path
import json
import xlrd
import xlwt
import time
import random

import subprocess

# sys.argv
stockIDs=["2330","2331","2332","2333"]
# sys.argv
dateTimes=["20210131","20210228","20210331"]
for stockID in stockIDs:
    for dateTime in dateTimes:
        # python "個股日成交資訊-方法2.py"  "2330"  "20210131"
        responeStr = subprocess.check_output(['python', '個股日成交資訊-方法2.py',stockID,dateTime])
        responeStr = responeStr.decode("utf-8")
        print(responeStr)
        delayTime=int(random.random() * 20) + 10 # 10 ~70 sec 的亂數
        time.sleep(delayTime)