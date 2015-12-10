# -*- coding: utf-8 -*-
"""
Mydaily-web-version-1.0
Author Shenlang
Start: 2015.11.12 10:30

"""

import sys, sae
import sae.kvdb
from flask import Flask, request, render_template
from time import strftime, localtime

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

def classify_items(tag, item):
    kv = sae.kvdb.Client()
    c = kv.get(str(tag))
    if not c:
        item_in_tag = []
        item_in_tag.append(item)
        
        kv.set(tag, item_in_tag)    
    else:
        item_in_tag = c.append(item)
        kv.replace(tag, item_in_tag)
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
    kv.disconnect_all()
    classify_items(tag, key)
    

#def collect_tags(tag):
#    kv = sae.kvdb.Client()
#    if kv.get('tags'):
#        tags_set = kv.get('tags')
#        for key,value in tags_set:
#            if tag == key:
#                value += 1
#                tags_set[tag]=value
#                kv.repalce('tags',tags_set)
#            else:
#                value = 1
#                tags_set[tag]=value
#                kv.replace('tags',tags_set)
#    else:
#        tags_set = {}
#        kv.set('tags', tags_set)
#    kv.disconnect_all()

def check_tags(tag):
    if not tag:
        return 'NULL'
    else:
        return tag

def read_KVDB():
    kv = sae.kvdb.Client()
    internal_content = kv.get_by_prefix('No', 100)
    return internal_content
    kv.disconnect_all()


@app.route('/mydaily')#@app.route('/login', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/mydaily', methods=['POST'])
def save_mydaily():
    """ receive input and show database content in the browser
    """  
    content = request.form['content']
    tag = request.form['tag']
    tag = check_tags(tag)
    #collect_tags(tag)
    save_and_classify(content, tag)
    previous_content = read_KVDB()
    print previous_content 
    return render_template('template.html', rows=previous_content)
        

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



if __name__ == '__main__':
    app.run()