# -*- coding: utf-8 -*-
#qpy:webapp:Mydaily
#qpy:fullscreen
#qpy://localhost:8080/

"""
Appname: Mydaily-Android
Author: Shenlang
Start: 2015.11.30

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


def classify_items(tag, item):
    kv = sae.kvdb.Client()
    if kv.get(tag):
        item_in_tag = kv.get(tag).append(item)
        kv.replace(tag, item_in_tag)
    else:
        item_in_tag = []
        item_in_tag.append(item)
        kv.set(tag, item_in_tag)
    kv.disconnect_all()   

def count_items():
    kv = sae.kvdb.Client()
    if kv.get('NumberOfItems'):
        item_number = 0
        item_number = kv.get('NumberOfItems') + 1
        kv.replace('NumberOfItems', item_number)
        return item_number
    else:
        kv.set('NumberOfItems', 1)
        return 1
    kv.disconnect_all()
    


def save_and_classify(content, tag):
    """
    """
    time = strftime("%y\%m\%d-%H:%M:%S", localtime())
    kv = sae.kvdb.Client()
    item_number = count_items()
    key = 'No.' + str(item_number)
    value = {'time':time, 'content':content, 'tag': tag}
    kv.set(key, value)
    classify_items(tag, key)
    kv.disconnect_all()

def collect_tags(tag):
    kv = sae.kvdb.Client()
    tags_set = {}
    kv.set('tags', tags_set) 
    tags_set = kv.get('tags')
    for key,value in tags_set:
        if tag == key:
            value += 1
            tags_set[tag]=value
            kv.repalce('tags',tags_set)
        else:
            value = 1
            tags_set[tag]=value
            kv.replace('tags',tags_set)
    kv.disconnect_all()

def check_tags(tag):
    if not tag:
        return 'NULL'
    else:
        return tag

def read_KVDB():
    kv = sae.kvdb.Client()
    content = kv.get_by_prefix('No', 100)
    return content
    kv.disconnect_all()


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
    content = request.forms.get('content')
    tag = request.forms.get('tag')
    tag = check_tags(tag)
    collect_tags(tag)
    save_and_classify(content, tag)
    previous_content = read_KVDB()
 #   for k,v in previous_content:
 #       print k,v    
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
        previous_content = read_KVDB()
        content = '\n'.join([value['time']+'>>'+value['content']+'<<'
                    'tag:'+value['tag'] for key, value in previous_content])
        print content
        return content

        kv.disconnect_all()       
    elif message_from_client == "tag":
        tag_message = request.forms.get('tag')
        kv = sae.kvdb.Client()
        items = kv.get(tag_message)
        items_content = kv.get_multi(items)
        kv.disconnect_all()
    elif message_from_client == "da":
        kv = sae.kvdb.Client()
        kv.delete('')
        return "Done!"
        kv.disconnect_all()
    else:
        return "Sorry, 请阅读HELP"

application = sae.create_wsgi_app(app)