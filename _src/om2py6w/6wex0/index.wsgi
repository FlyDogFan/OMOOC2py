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

def check_event(msg_dict):
    toUser = msg_dict['ToUserName']
    fromUser = msg_dict['FromUserName']
    if msg_dict['Event'] == "subscribe":
        reply_text = u'''欢迎订阅, 开始记录你的点点滴滴吧~
                         w: write something
                         r: read what you have written
                         h: help'''
        return self.render.reply(fromUser, toUser,int(time.time()),reply_text)
    elif msg_dict['Event'] == "unsubscribe":
        reply_text = u'''这就退订了? 确定不后悔? 再订还可以呢啊. 没给你拉黑名单!'''
        return self.render.reply(fromUser,toUser,int(time.time()),reply_text) 
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


@app.route('/', method="POST")
def mydaily():
    msg_dict = parse_message()
    if msg_dict['Msgtype'] == "event":
        return check_event( msg_dict )
    else: 
        save_message(msg_dict)
        return 



application = sae.create_wsgi_app(app)   