#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mydaily-web-version-1.0
Author Shenlang
Start: 2015.11.5 10:30
add: bottle 
     jinja2
     Database
     websocket
"""

import sys, sqlite3
from bottle import Bottle, route, abort, request  
from jinja2 import Template, Environment, PackageLoader ,FileSystemLoader
from gevent import monkey; monkey.patch_all()
from time import sleep
from datetime import date


reload(sys)
sys.setdefaultencoding('utf-8')

app = Bottle()

template_loader = FileSystemLoader('views')
env = Environment(loader=template_loader)


def insert_data(data):
    """insert data from input to Database
    """
    db = sqlite3.connect('mydaily_data.db')
    c = db.cursor()
    c.execute('INSERT INTO mydaily_data VALUES (?,?)', data)
    db.commit()
    db.close()


def fetch_data():
    """fetch data from database
       add ':' between every item
    """
    db = sqlite3.connect('mydaily_data.db')
    c = db.cursor()
    c.execute('SELECT * FROM mydaily_data')
    b = c.fetchall()
    d = []
    for member in b:
        a = "%s : %s\n"% member
        d.append(a)
    return d 
    db.close()


def only_fetch_data():
    """ fetch data from database
        add ':' between every item
    """
    db = sqlite3.connect('mydaily_data.db')
    c = db.cursor()
    c.execute('SELECT * FROM mydaily_data')
    b = c.fetchall()
    return b


@app.route('/')
@app.route('/mydaily')
def mydaily():
    """home page
    """
    template_1 = env.get_template('home.tpl')
    return template_1.render()
    

@app.route('/mydaily', method='POST')
def save_mydaily():
    """ receive input and show database content in the browser
    """ 
    daily_content = request.forms.get('content')
    now = date.today()
    data = daily_content
    print "srv.got:", data
    if daily_content:
        data = now, daily_content.decode("utf-8")
        insert_data(data)
        previous_content = fetch_data()
        template_2 = env.get_template('template.tpl')
        return template_2.render(rows=previous_content)


@app.route('/client')
def client():
    """This is designed for terminal interaction.
    """
    wsock = request.environ.get('wsgi.websocket')
    if not wsock:
        abort(400, 'Expected WebSocket request.')
    while True:
        try:
            message = wsock.receive()
            if message == "pre":
            	previous_content = only_fetch_data()
                wsock.send(previous_content)
                sleep(3)
                wsock.send(previous_content)
        except WebSocketError:
            break        


from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler

server = WSGIServer(("localhost", 8080), app,
                    handler_class=WebSocketHandler)

server.serve_forever()


