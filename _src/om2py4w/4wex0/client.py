# _*_ coding:utf-8 _*_
#! /usr/bin/env python
"""
client


"""
from websocket import create_connection

ws = create_connection("ws://localhost:8080/client")
msg = raw_input('> ')
ws.send(msg)

print "Receiving..."
result =  ws.recv() 
print result

ws.close()

