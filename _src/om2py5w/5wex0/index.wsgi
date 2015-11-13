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
    if daily_content:
        time = strftime("%y\%m\%d-%H:%M:%S", localtime())
        kv = sae.kvdb.Client()
        kv.set(time,daily_content)
        previous_content = kv.get_by_prefix('', 100)
        template_2 = env.get_template('template.tpl')
        return template_2.render(rows=previous_content)


application = sae.create_wsgi_app(app)