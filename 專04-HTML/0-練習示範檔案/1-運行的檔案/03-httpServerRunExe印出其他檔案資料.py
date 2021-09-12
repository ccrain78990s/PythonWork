# -*- coding: UTF-8 -*-
__author__ = "Powen Ko, www.powenko.com"

import sys
import time
import os

import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import urlparse
import subprocess


"""
http://127.0.0.1:8888/?name=abc&password=123

"""
class MyHandler(RequestHandler):


    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        out_bytes = subprocess.check_output(['python','test.py'])
        self.wfile.write(out_bytes)

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8888

print('Server listening on port %s' % port)
socketserver.TCPServer.allow_reuse_address = True
#httpd = socketserver.TCPServer(('127.0.0.1', port), MyHandler)
httpd = socketserver.TCPServer(('0.0.0.0', port), MyHandler)
try:
    httpd.serve_forever()
except:
    print("Closing the server.")
    httpd.server_close()
    raise
