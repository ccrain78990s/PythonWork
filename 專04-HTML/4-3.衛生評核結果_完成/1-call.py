# -*- coding: UTF-8 -*-
__author__ = "Chen"

import sys
import time
"""
109年度餐飲衛生管理分級評核結果 (新竹)
http://127.0.0.1:8888/?action=restaurantall

http://127.0.0.1:8888/?action=restaurant&level=優
http://127.0.0.1:8888/?action=restaurant&level=良


"""

import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import urlparse,unquote
import subprocess

class MyHandler(RequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        html = '讀取資料 '
        print(self.path)                   # /?name=powenko&passsword=abc
        query = urlparse(self.path).query  #  'name=powenko&passsword=abc'
        if query!="":
           dict2 = dict(qc.split("=") for qc in query.split("&"))
           try:
                action = dict2["action"].lower()
                print(action)
                if action=="restaurantall":
                    # html ="顯示評核餐廳的所有資料"
                    print("測試")
                    html = subprocess.check_output(['python', '2-restaurant.py'])
                    print("OK")

                    self.wfile.write(html)
                    return

                if action=="restaurant":
                    print(dict2["level"])
                    level = unquote(dict2["level"].lower())   # URL 的資料, 轉成utf-8文字
                    html = subprocess.check_output(['python', '3-level.py',level])
                    # python 3-level.py  優/良
                    self.wfile.write(html)
                    return

           except:
                html=html+"資料讀取失敗(請重新連結或是更換網址)"
        html = html.encode("utf-8")
        self.wfile.write(html)


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
