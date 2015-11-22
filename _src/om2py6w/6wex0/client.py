#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mydaily-wechat-client
Author Shenlang

"""

import sys,requests
import time
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    while True:
        textTpl = """<xml>
                 <ToUserName><![CDATA[%s]]></ToUserName>
                 <FromUserName><![CDATA[%s]]></FromUserName> 
                 <CreateTime>%s</CreateTime>
                 <MsgType><![CDATA[text]]></MsgType>
                 <Content><![CDATA[%s]]></Content>
                 <MsgId>1234567890123456</MsgId>
                 </xml>"""  
        send_content = raw_input('> ')
        echostr = textTpl % ('qqqq', 'wwww', int(time.time()), send_content)
        r = requests.post('http://localhost:8080/', echostr)
        rr = requests.get('http://localhost:8080/')
        print r.content, rr.content

if __name__ == '__main__':
    main()