# _*_ coding:utf-8 _*_
#! /usr/bin/env python
'''
客户端
'''
from websocket import create_connection

ws = create_connection("ws://localhost:8080/mydaily")
msg = raw_input('> ')
ws.send(msg)
print "Sent"
print "Receiving..."
result =  ws.recv()
print "Received '%s'" % result
ws.close()
