# -*- coding: UTF-8 -*-
__author__ = "Chen"

import sys
import time
"""

# http://127.0.0.1:8888/?action=income_all 

"""

import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
import urllib.parse
from urllib.parse import urlparse
import subprocess

class MyHandler(RequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        html = '我收到資料 '
        print("連接網址:",self.path)                   # /?name=powenko&passsword=abc
        query = urlparse(self.path).query             #  'name=powenko&passsword=abc'
        if query!="":
           dict_ = dict(qc.split("=") for qc in query.split("&"))
           try:
                action =dict_["action"].lower()
                print(action)
                if action=="income_all":
                    # html ="顯示收入所有資料"
                    print("全部資料列印-Try")
                    html = subprocess.check_output(['python', '4.1-全部資料列印.py'])
                    print("全部資料列印-OK")

                    self.wfile.write(html)
                    return

                if action == "income":
                    print(dict_["rate"])
                    rate =unquote(dict_["rate"])  # URL 的資料, 轉成utf-8文字
                    html = subprocess.check_output(['python', '4.3-成長率.py', rate])
                    self.wfile.write(html)
                    return


           except:
                html=html+"資料讀取失敗"
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
