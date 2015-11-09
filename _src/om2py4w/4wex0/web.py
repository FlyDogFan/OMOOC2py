#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mydaily-web-version-1.0
使用bottle框架
加入jinja2
开始时间: 2015.11.5 10:30

"""

import sys
from bottle import * # 慎用, 会引入很多未知的东西, 或者全局变量神马的.
from jinja2 import *  #Template, Environment, PackageLoader

reload(sys)
sys.setdefaultencoding('utf-8')

template_loader = FileSystemLoader('templates')
env = Environment(loader=template_loader)

#from bottle import route, get, post, request, error, run

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
            f.close()


#@error(404)# 404
#def error404(error):
#    return 'Nothing here, sorry'

if __name__ == '__main__':
    debug(True)
    run(host="localhost", port=8080, reloader=True)











