0# -*- coding: UTF-8 -*-
__author__ = "Chen"
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

"""

import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import urlparse,unquote
import subprocess
import aiml


auth_token='6aDnidTkzzweW2ed4Ijggf5CItXQJGoDMvbEpLoKrvqDDjRFRzZPa8T4fu8TlPhTeHrd5idrQG3haDtDSTJwkcG6M3Eqgm+AJR6OLIppsLVVnw2V1CN9VMm0sTV6Sp0ZrBmCqyoW2Y4a4GEBcg8f2gdB04t89/1O/w1cDnyilFU='
userId = "U936a8a4a4f642ad8172501d59d8d766c"

class MyHandler(RequestHandler):
    def strResponse(self,text,userId,data):
        global kernel
        responeStr="沒有資料"
        if (text=="hi"):
            responeStr="你好"
        if text.lower()=="顯示住宿所有資料":
            responeStr = subprocess.check_output(['python', '07HTTP_JSON-openData-Ubike.py'])
            responeStr = responeStr.decode("utf-8")
        # 寫法1
        elif text.lower() == "顯示龜山區住宿的資料":
            sarea="龜山區"
            responeStr = subprocess.check_output(['python', '07HTTP_JSON-openData-UbikeBysarea.py', sarea])
            responeStr = responeStr.decode("utf-8")
        # 寫法2
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
            #AIML
            responeStr = kernel.respond(text)
            # AIML > 抓取OPEN DATA
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
            "replyToken":replyToken,      # 回答的模式
            "messages": [
                {
                    "type": "text",
                    "text": responeStr,   # 傳給用戶字串
                }
            ]
        }



        hed = {'Authorization': 'Bearer ' + auth_token}
        url = 'https://api.line.me/v2/bot/message/reply'
        response = requests.post(url, json=message, headers=hed)
        print(response)
        print(response.json())



kernel = aiml.Kernel()
kernel.learn("AIML.xml")
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



