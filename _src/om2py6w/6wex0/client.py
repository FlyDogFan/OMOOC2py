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
    
#    if input_content == "tag":
#    r2 = requests.post('http://localhost:8080/mydaily/client', 
#        	                data = {tag_input})
#   	tag_input = raw_input('Please write your tag > ')
#      r2 = requests.post('http://localhost:8080/mydaily/client', 
#     	                tag = {tag_input})
#       else:
#        r3 = requests.post('http://localhost:8080/mydaily/client', 
# 	                data = {input_content})
    
    rr = requests.get('http://localhost:8080/')
    print r.content, rr.content

if __name__ == '__main__':
    main()