#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mydaily-web-version-1.0
使用bottle框架
开始时间: 2015.11.5 10:30

"""


from bottle import *


#@route('/hello/<name>')
#def index(name):
#    return template('<b>Hello {{name}}</b>!', name=name)

@route('/login')
def login():
	return '''
	    <form action="/login" method="post">
用户: <input name ="uname" type="text" />
口令: <input name ="passw" type="password" />
<input value ="Login" type="submit" />
      </form>
      '''	    
@route('/login', method='POST')
def do_login():
	username = request.forms.get('uname')
	password = request.forms.get('passw')
	print "srv.got:", username, password
	if username:
		return template("<p>Done!<hr/>{{ name }}<p>"
		         , name=username)	    



if __name__ == '__main__':
    debug(True)
    run(host="localhost", port=8080, reloader=True)











