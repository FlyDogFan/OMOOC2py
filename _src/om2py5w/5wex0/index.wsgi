#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mydaily-web-version-1.0
Author Shenlang
Start: 2015.11.12 10:30

"""

import sys, sae
import sae.kvdb
from bottle import Bottle, route, abort, request, run  
from jinja2 import Template, Environment, PackageLoader ,FileSystemLoader
from time import strftime, localtime
#from array import *

reload(sys)
sys.setdefaultencoding('utf-8')

app = Bottle()

template_loader = FileSystemLoader('views')
env = Environment(loader=template_loader)

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
    tag = request.forms.get('tag')
    if not tag:
        tag = "NULL"
    if daily_content:
        time = strftime("%y\%m\%d", localtime())
        message = {'time':time, 'daily_content':daily_content}
        kv = sae.kvdb.Client()
        kv.add(tag,message)
        previous_content = kv.get_by_prefix('', 100)
        template_2 = env.get_template('template.tpl')
        return template_2.render(rows=previous_content)


@app.route('/client')
def client():
    """This is designed for terminal interaction.
    """
    message_from_client = request.forms.get('data')
    if message_from_client == "pre":
        content = ''
        kv = sae.kvdb.Client()
        previous_content = kv.getkeys_by_prefix('', 100)
        content = '\n'.join([row[0]+'>>'+row[1] for row in previous_content])
        return content
    elif message_from_client == "flush":
        kv = sae.kvdb.Client()
        kv.delete('')
        return "Done!"
    else:
        return "Sorry, 请阅读帮助文档..还没弄"

application = sae.create_wsgi_app(app)