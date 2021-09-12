# -*- coding: UTF-8 -*-
__author__ = "Chen"

import sys
import time
"""

# http://127.0.0.1:8888/?action=UbikeAll 

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

        html = '我收到資料 '
        print("連接網址:",self.path)                   # /?name=powenko&passsword=abc
        query = urlparse(self.path).query  #  'name=powenko&passsword=abc'
        if query!="":
           dict2 = dict(qc.split("=") for qc in query.split("&"))
           try:
                action = dict2["action"].lower()
                print(action)
                if action=="income_all":
                    # html ="顯示Ubike 所有資料"
                    print("全部資料列印-Try")
                    html = subprocess.check_output(['python', '4.1-全部資料列印.py'])
                    print("全部資料列印-OK")

                    self.wfile.write(html)
                    return
                """
                if action=="ubike":
                    print(dict2["sarea"])
                    sarea = unquote(dict2["sarea"].lower())   # URL 的資料, 轉成utf-8文字
                    html = subprocess.check_output(['python', '07HTTP_JSON-openData-UbikeBysarea.py',sarea])
                    # python 07HTTP_JSON-openData-UbikeBysarea.py  龜山區
                    self.wfile.write(html)
                    return
                """

           except:
                html=html+"沒有資料"
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
