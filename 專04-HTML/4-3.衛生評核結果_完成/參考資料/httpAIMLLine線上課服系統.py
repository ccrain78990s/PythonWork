0# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"
from sys import version as python_version
from cgi import parse_header, parse_multipart
import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import parse_qs
import json
import requests
import sys
import time
"""
#第一步:
#  Ubike 顯示  轉成網頁
#  simplehttp  +   Ubike  把全部的資料

# http://127.0.0.1:8888/?action=UbikeAll 

# 第二步:
顯示真的Ubike 資料 

# 第三步:
# 做一個 html 網頁, 點選後 a  link  顯示 全部的區域

# 第四步:
# 點選 link ,  顯示該區域的ubike 資料
http://127.0.0.1:8888/?action=Ubike&sarea=龜山區
http://127.0.0.1:8888/?action=Ubike&sarea=中壢區
http://127.0.0.1:8888/?action=Ubike&sarea=桃園區

http://127.0.0.1:8888/?aiml=公司電話
 
# HTML + Javascript + PHP/ASP + Python

"""

import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import urlparse,unquote
import subprocess
import aiml


auth_token='6aDnidTkzzweW2ed4Ijggf5CItXQJGoDMvbEpLoKrvqDDjRFRzZPa8T4fu8TlPhTeHrd5idrQG3haDtDSTJwkcG6M3Eqgm+AJR6OLIppsLVVnw2V1CN9VMm0sTV6Sp0ZrBmCqyoW2Y4a4GEBcg8f2gdB04t89/1O/w1cDnyilFU='
userId = "U24b70d9be4685a37aab45333365fccca"

class MyHandler(RequestHandler):
    def strResponse(self,text,userId,data):
        global kernel
        responeStr="沒有資料"
        if (text=="hi"):
            responeStr="你好"
        if text.lower()=="顯示ubike所有資料":
            responeStr = subprocess.check_output(['python', '07HTTP_JSON-openData-Ubike.py'])
            responeStr = responeStr.decode("utf-8")
        elif text.lower() == "顯示龜山區ubike的資料":
            sarea="龜山區"
            responeStr = subprocess.check_output(['python', '07HTTP_JSON-openData-UbikeBysarea.py', sarea])
            responeStr = responeStr.decode("utf-8")
        elif text.lower().find("顯示")>=0  and  text.lower().find("ubike的資料")>=0:
            # "顯示中壢區ubike的資料"
            # "顯示八德區ubike的資料"
            t1=text.lower().find("顯示")+2
            t2=text.lower().find("ubike的資料")
            sarea=text[t1:t2]   # 抓出中間的 文字  # 八德區
            print(sarea,text,t1,t2)
            responeStr = subprocess.check_output(['python', '07HTTP_JSON-openData-UbikeBysarea.py', sarea])
            responeStr = responeStr.decode("utf-8")
        else:
            responeStr = kernel.respond(text)

            if (responeStr.find('exe') > 0):
                data = json.loads(responeStr)
                print(data)
                exe2 = data["exe"]
                exe2List=exe2.split()    # 用 空白  把 文字  轉成list   ['python','07HTTP_JSON-openData-UbikeBysarea.py','中壢區']
                responeStr = subprocess.check_output(exe2List)   # 執行程式 並把 print 傳到  responeStr 變數中
                responeStr = responeStr.decode("utf-8")      # 把bytes 轉 字串str


        if responeStr=="":  #
            responeStr="沒有資料"

        #if text=="xxx":
        #    return "hello"
        return responeStr

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        global auth_token,userId
        varLen = int(self.headers['Content-Length'])
        if varLen > 0:
            post_data = self.rfile.read(varLen)
            data = json.loads(post_data)
            print(data)
            replyToken=data['events'][0]['replyToken']
            userId=data['events'][0]['source']['userId']
            text=data['events'][0]['message']['text']     # 用戶傳過來的字串

            responeStr=self.strResponse(text,userId,data) # 處理的函數

            # responeStr="Your User Id: "+userId+"\nText:"+text  # 傳給用戶字串
        self.do_HEAD()
        # print(self.wfile)
        message = {
            "replyToken":replyToken,
            "messages": [
                {
                    "type": "text",
                    "text": responeStr,   # 傳給用戶字串
                }
            ]
        }
        """
        # https://developers.line.biz/en/docs/messaging-api/message-types/
        message = {
            "replyToken": replyToken,
            "messages": [
                {
                        "type": "image",
                        "originalContentUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Argentinosaurus_skeleton%2C_PLoS_ONE.png/1280px-Argentinosaurus_skeleton%2C_PLoS_ONE.png",
                        "previewImageUrl":"https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Argentinosaurus_skeleton%2C_PLoS_ONE.png/1280px-Argentinosaurus_skeleton%2C_PLoS_ONE.png"
                }
            ]
        }
        """

        hed = {'Authorization': 'Bearer ' + auth_token}
        url = 'https://api.line.me/v2/bot/message/reply'
        response = requests.post(url, json=message, headers=hed)
        print(response)
        print(response.json())

    def do_GET(self):
        self.do_POST()

        global kernel
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        html = '我收到資料 '
        print(self.path)                   # /?name=powenko&passsword=abc
        query = urlparse(self.path).query  #  'name=powenko&passsword=abc'
        if query!="":
           dict2 = dict(qc.split("=") for qc in query.split("&"))
           try:
                aiml=""
                action=""
                if "aiml" in dict2:
                    aiml = dict2["aiml"].lower()      #<--
                    print(aiml)
                if "action" in dict2:
                    action = dict2["action"].lower()  #<---
                    print(action)
                if aiml!="":
                    print(aiml)
                    aiml = unquote(aiml.lower())   # URL 的資料, 轉成utf-8文字
                    print(aiml)
                    html=kernel.respond(aiml)
                    print(html)
                    html=html.encode("utf-8")  # string to bytes
                    self.wfile.write(html)
                    return
                if action=="ubikeall":
                    # html ="顯示Ubike 所有資料"
                    print("1111")
                    html = subprocess.check_output(['python', '07HTTP_JSON-openData-Ubike.py'])
                    print("222")
                    self.wfile.write(html)
                    return
                if action=="ubike":
                    print(dict2["sarea"])
                    sarea = unquote(dict2["sarea"].lower())   # URL 的資料, 轉成utf-8文字
                    html = subprocess.check_output(['python', '07HTTP_JSON-openData-UbikeBysarea.py',sarea])
                    # python 07HTTP_JSON-openData-UbikeBysarea.py  龜山區
                    self.wfile.write(html)
                    return

           except:
                html=html+"沒有資料"
        html = html.encode("utf-8")
        self.wfile.write(html)


kernel = aiml.Kernel()
kernel.learn("01-AIML-公司客服系統.xml")
# kernel.respond("load aiml b")  # 請參考 05-AIML-load.xml

port = 8888
print('Server listening on port %s' % port)
socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('0.0.0.0', port), MyHandler)
try:
    httpd.serve_forever()
except:
    print("Closing the server.")
    httpd.server_close()
    raise



