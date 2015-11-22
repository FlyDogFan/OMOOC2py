# -*- coding: utf-8 -*-
"""
Mydaily-wechat
Author Shenlang

"""
import sys, sae
import hashlib
import sae.kvdb 
import time
from bottle import Bottle, route, abort, request, run
import xml.etree.ElementTree as ET

reload(sys)
sys.setdefaultencoding('utf-8')


app = Bottle()


def count_items():
    kv = sae.kvdb.Client()
    if kv.get('NumberOfItems'):
        item_number = 0
        item_number = kv.get('NumberOfItems') + 1
        kv.replace('NumberOfItems', item_number)
        return item_number
    else:
        kv.set('NumberOfItems', 1)
        return 1
    kv.disconnect_all()

def parse_message():
    message = request.body.read()
    root = ET.fromstring(message)
    msg_dict = {}
    for child in root:
        msg_dict[child.tag] = child.text
    return msg_dict

def save_message(msg):
    kv = sae.kvdb.Client()
    item_number = count_items()
    key = 'No.' + str(item_number)
    kv.set(key, msg)
    kv.disconnect_all()
    return item_number

def check_event(msg_dict):
    textTpl = """<xml>
                 <ToUserName><![CDATA[%s]]></ToUserName>
                 <FromUserName><![CDATA[%s]]></FromUserName>
                 <CreateTime>%s</CreateTime>
                 <MsgType><![CDATA[%s]]></MsgType>
                 <Content><![CDATA[%s]]></Content>
                 </xml>"""
    if msg_dict['Event'] == "subscribe" :   
        reply_text = u'''欢迎订阅!
                        w: write something
                        r: read what you have written
                        h: help'''
        echostr = textTpl % (
            msg_dict['FromUserName'], msg_dict['ToUserName'], int(time.time()),  
                    'text',reply_text)
        return echostr
    elif msg_dict['Event'] == "unsubscribe":
        reply_text = u'''这就退订了? 确定不后悔? 再订还可以呢啊. 没给你拉黑名单!'''
        echostr = textTpl % (
                msg_dict['FromUserName'], msg_dict['ToUserName'], int(time.time()),  
                    'text',reply_text)
        return echostr
    else:
        return None

@app.route('/')
def CheckSignature():
    token = "xpgeng" 
    signature = request.GET.get('signature', None)
    timestamp = request.GET.get('timestamp', None)
    nonce = request.GET.get('nonce', None)
    echostr = request.GET.get('echostr', None)
    tmpList = [token, timestamp, nonce]
    tmpList.sort()
    tmpstr = "%s%s%s" % tuple(tmpList)
    hashstr = hashlib.sha1(tmpstr).hexdigest()
    if hashstr == signature:
        return echostr
    else:
        return None


@app.route('/', method='POST')
def mydaily():
    msg_dict = parse_message()
    textTpl = """<xml>
                 <ToUserName><![CDATA[%s]]></ToUserName>
                 <FromUserName><![CDATA[%s]]></FromUserName>
                 <CreateTime>%s</CreateTime>
                 <MsgType><![CDATA[%s]]></MsgType>
                 <Content><![CDATA[%s]]></Content>
                 </xml>"""
    if msg_dict['MsgType'] == 'event':
        return check_event(msg_dict)
    elif msg_dict['Content'][2] == '.':
        print msg_dict['Content'][2]
        item_number = save_message(msg_dict)
        reply_text = u'''Roger that. 这是第%s条日记.''' % item_number
        echostr = textTpl % (
                msg_dict['FromUserName'], msg_dict['ToUserName'], int(time.time()),  
                    msg_dict['MsgType'],reply_text)
        return echostr
    elif msg_dict['Content'] == 'h':
        reply_text = u'''w: write something
                         r: read what you have written
                         h: help'''
        echostr = textTpl % (
                msg_dict['FromUserName'], msg_dict['ToUserName'], int(time.time()),  
                    msg_dict['MsgType'],reply_text)
        return echostr
    #elif msg_dict['Content'] == 'r':
    else:
        return None

application = sae.create_wsgi_app(app)   