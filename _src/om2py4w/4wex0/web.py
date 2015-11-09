#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mydaily-web-version-1.0
使用bottle框架
加入jinja2
开始时间: 2015.11.5 10:30

"""

import sys, socket
from datetime import date
from bottle import * # 慎用, 会引入很多未知的东西, 或者全局变量神马的.
from jinja2 import *  #Template, Environment, PackageLoader

reload(sys)
sys.setdefaultencoding('utf-8')

template_loader = FileSystemLoader('templates')
env = Environment(loader=template_loader)

#from bottle import route, get, post, request, error, run

def save(data):
    with open('diary.md','a') as f:
        now = date.today()
        f.writelines("%s\n\n%s\n\n"%(now,data)) 


def read_diary():
    with open('diary.md','r') as f:
        return f.read()


@route('/mydaily')
def mydaily():
    template_1 = env.get_template('home.html')
    return template_1.render()


@route('/mydaily', method='POST')
def save_mydaily():
    daily_content = request.forms.get('content')
    print "srv.got:", daily_content
    if daily_content:
        with open('diary.md','a') as f:
            f.write("%s\n\n" %daily_content)
            f.close() 
        with open('diary.md','r') as f:           
            previous_content = f.read()
            template_2 = env.get_template('template.html')
            return template_2.render(name=previous_content)
            print previous_content
            f.close()


BUF_SIZE = 1024  
server_address = ('localhost', 8080)  
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
server.bind(server_address)
while True: 
    data, client_address = server.recvfrom(BUF_SIZE)  
    if not data:  
        print "client has exist"  
        break  
    elif data == "pre":        
        message = read_diary()
        server.sendto(message, client_address)    
    else :
        save(data)
        print "received:", data, "from", client_address    
server.close()


#@error(404)# 404
#def error404(error):
#    return 'Nothing here, sorry'

if __name__ == '__main__':
    debug(True)
    run(host="localhost", port=8080, reloader=True)











