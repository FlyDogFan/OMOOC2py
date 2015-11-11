# _*_ coding:utf-8 _*_
#! /usr/bin/env python
'''
客户端
'''
from websocket import create_connection

ws = create_connection("ws://localhost:8080/client")
msg = raw_input('> ')
ws.send(msg)
print "Sent"
print "Receiving..."
result =  ws.recv()

for item in result.split():
	print item

#for item in result:
#    print "Received '%s'" % item
ws.close()

