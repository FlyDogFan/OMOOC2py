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
        reply_text = u'''欢迎使用!目前的功能为
                        .+输入内容: write something
                         r: read what you have written
                         h: help
                         d+数字:删除该条笔记
                         c: clear all'''
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

def read_KVDB():
    kv = sae.kvdb.Client()
    content = kv.get_by_prefix('No', 100)
    return content
    kv.disconnect_all()


def check_tag(msg_dict_content):
    number = 0
    if "#" not in msg_dict_content:
        tag_none = "NULL"
        return tag_none, number
    else:
        for string in msg_dict_content:
            number += 1
            if string == '#':
                tag_exist = msg_dict_content[number:]
                return tag_exist, number


def delete_item(search_key):
    kv = sae.kvdb.Client()
    kv.delete(search_key)
    kv.disconnect_all()
    return "Done!"

def delete_all():
    kv = sae.kvdb.Client()
    keys=kv.getkeys_by_prefix('No', 100)
    for item in keys:
        kv.delete(item)
    kv.disconnect_all()
    return "Done!"

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
    elif msg_dict['Content'][0] == '.':
        tag = check_tag( msg_dict['Content'])[0]
        string_number = check_tag( msg_dict['Content'])[1]
        if tag == "NULL":
            real_content = msg_dict['Content'][1:]
        else:
            real_content = msg_dict['Content'][1:(string_number-1)]
        msg_dict['Content'] = real_content
        msg_dict['Tag'] = tag
        item_number = save_message(msg_dict)
        reply_text = u'''Roger that. 这是第%s条日记.''' % item_number
        echostr = textTpl % (
                msg_dict['FromUserName'], msg_dict['ToUserName'], 
                int(time.time()), msg_dict['MsgType'],reply_text)
        return echostr
    elif msg_dict['Content'] == 'h':
        reply_text = u'''.+输入内容: write something
                         r: read what you have written
                         h: help
                         d+数字:删除该条笔记
                         c: clear all'''
        echostr = textTpl % (
                msg_dict['FromUserName'], msg_dict['ToUserName'],
                int(time.time()), msg_dict['MsgType'],reply_text)
        return echostr
    elif msg_dict['Content'] == 'r':
        db_content = read_KVDB()
        all_content = '\n'.join(value['Content']+'#Tag:'+ 
                                value['Tag']+'#' for key, value in db_content)
        print all_content
        reply_text = u'''%s''' % all_content
        echostr = textTpl % (
                msg_dict['FromUserName'], msg_dict['ToUserName'], 
                int(time.time()), msg_dict['MsgType'],reply_text)
        return echostr
    elif msg_dict['Content'][0] == 'd':
        delete_number = msg_dict['Content'][1:]
        search_key = 'No.'+delete_numbers
        return_text = u'''%s已经删除第%s条日记'''%(delete_item(search_key),
                                    delete_number)
        echostr = textTpl % (
                msg_dict['FromUserName'], msg_dict['ToUserName'], 
                int(time.time()), msg_dict['MsgType'],return_text)
        return echostr
    elif msg_dict['Content'] == "c":
        result = delete_all()
        result_text = u'''%s已经删除全部内容'''% result
        echostr = textTpl % (
                msg_dict['FromUserName'], msg_dict['ToUserName'], 
                int(time.time()), msg_dict['MsgType'],result_text)
        return echostr
    else:
        reply_text = u'''.+输入内容: write something
                         r: read what you have written
                         h: help
                         d+数字:删除该条笔记
                         c: clear all'''
        echostr = textTpl % (
                msg_dict['FromUserName'], msg_dict['ToUserName'], 
                int(time.time()), msg_dict['MsgType'],reply_text)
        return echostr

application = sae.create_wsgi_app(app)   