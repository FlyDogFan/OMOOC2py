#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mydaily-web-version-1.0
使用bottle框架
加入jinja2
加入 Database
开始时间: 2015.11.5 10:30

"""

import sys, sqlite3
from datetime import date
from bottle import * # 慎用, 会引入很多未知的东西, 或者全局变量神马的.
from jinja2 import *  #Template, Environment, PackageLoader
from datetime import date

reload(sys)
sys.setdefaultencoding('utf-8')

app = Bottle()

template_loader = FileSystemLoader('templates')
env = Environment(loader=template_loader)

@app.route('/mydaily')
def mydaily():
    template_1 = env.get_template('home.html')
    return template_1.render()


@app.route('/mydaily', method='POST')
def save_mydaily():
    daily_content = request.forms.get('content')
    db = sqlite3.connect('mydaily_data.db')
    c = db.cursor()
    now = date.today()
    print "srv.got:", daily_content
    if daily_content:
        data = now, daily_content
        c.execute('INSERT INTO mydaily_data VALUES (?,?)', data)
        c.execute('SELECT * FROM mydaily_data')
        previous_content = c.fetchall()
        c.close()
        template_2 = env.get_template('template.tpl')
        return template_2.render(rows=previous_content)        


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











