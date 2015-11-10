#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mydaily-web-version-1.0
使用bottle框架
加入jinja2
加入 Database
开始时间: 2015.11.5 10:30

"""

import sys, sqlite3, json
from datetime import date
from bottle import * # 慎用, 会引入很多未知的东西, 或者全局变量神马的.
from jinja2 import *  #Template, Environment, PackageLoader
from datetime import date
from gevent import monkey; monkey.patch_all()
from time import sleep


reload(sys)
sys.setdefaultencoding('utf-8')

app = Bottle()

template_loader = FileSystemLoader('views')
env = Environment(loader=template_loader)

def insert_data(data):
    db = sqlite3.connect('mydaily_data.db')
    c = db.cursor()
    c.execute('INSERT INTO mydaily_data VALUES (?,?)', data)
    db.commit()
    db.close()

def fetch_data():
    db = sqlite3.connect('mydaily_data.db')
    c = db.cursor()
    c.execute('SELECT * FROM mydaily_data')
    return c.fetchall()
    db.close()


@app.route('/')
@app.route('/mydaily')
def mydaily():
    template_1 = env.get_template('home.tpl')
    return template_1.render()
    


@app.route('/mydaily', method='POST')
def save_mydaily():
    daily_content = request.forms.get('content')
    now = date.today()
    print "srv.got:", daily_content
    if daily_content:
        data = now, daily_content
        insert_data(data)
        previous_content = fetch_data()
        template_2 = env.get_template('template.tpl')
        return template_2.render(rows=previous_content)

@app.route('/client')
def client():
    wsock = request.environ.get('wsgi.websocket')
    if not wsock:
        abort(400, 'Expected WebSocket request.')
    while Ture:
        try:
            message = wsock.receive()
            if message == "pre":
                wsock.send("none")
                sleep(3)
                wsock.send("none")
        except WebSocketError:
            break        


from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler


server = WSGIServer(("localhost", 8080), app,
                    handler_class=WebSocketHandler)

server.serve_forever()




#@error(404)# 404
#def error404(error):
#    return 'Nothing here, sorry'

#if __name__ == '__main__':
#    debug(True)
#    run(host="127.0.0.1", port=8080, reloader=True)

