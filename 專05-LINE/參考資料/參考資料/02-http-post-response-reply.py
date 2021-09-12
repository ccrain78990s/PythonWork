from sys import version as python_version
from cgi import parse_header, parse_multipart
import socketserver as socketserver
import http.server
from http.server import SimpleHTTPRequestHandler as RequestHandler
from urllib.parse import parse_qs
import json
import requests
"""
https://developers.line.biz/en/reference/messaging-api/#send-reply-message


"""
"""
{
    'events': [
        {
            'type': 'message', 
            'replyToken': '57d8b671c639495cbdddb02b460e6e38', 
            'source': {
                'userId': 'U24b70d9be4685a37aab45333365fccca', 
                'type': 'user'
            }, 
            'timestamp': 1617867594327, 
            'mode': 'active', 
            'message': {
                'type': 'text', 
                'id': '13854956980015', 
                'text': 'Bbgg'
            }
        }
    ],
    'destination': 'U7a7085b932e86fa01c235554e57a696f'
}
"""
"""
Step1: 改 auth_token 和
Step2: ngrok http 8000  注意一下8000
Step3: https 回到Line 修改和打該  Webhook settings 

"""




auth_token='6aDnidTkzzweW2ed4Ijggf5CItXQJGoDMvbEpLoKrvqDDjRFRzZPa8T4fu8TlPhTeHrd5idrQG3haDtDSTJwkcG6M3Eqgm+AJR6OLIppsLVVnw2V1CN9VMm0sTV6Sp0ZrBmCqyoW2Y4a4GEBcg8f2gdB04t89/1O/w1cDnyilFU='

class MyHandler(RequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):

        userId="U24b70d9be4685a37aab45333365fccca"
        varLen = int(self.headers['Content-Length'])
        if varLen > 0:
            post_data = self.rfile.read(varLen)
            data = json.loads(post_data)
            print(data)
            replyToken=data['events'][0]['replyToken']
            userId=data['events'][0]['source']['userId']
            text=data['events'][0]['message']['text']

        self.do_HEAD()
        # print(self.wfile)
        message = {
            "replyToken":replyToken,
            "messages": [
                {
                    "type": "text",
                    "text": "Your User Id: "+userId+"\nText:"+text
                }
            ]
        }

        hed = {'Authorization': 'Bearer ' + auth_token}
        url = 'https://api.line.me/v2/bot/message/reply'
        response = requests.post(url, json=message, headers=hed)
        print(response)
        print(response.json())


socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('0.0.0.0', 8000), MyHandler)
httpd.serve_forever()
