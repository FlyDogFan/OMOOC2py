# -*- coding: utf-8 -*-
#qpy:webapp:Mydaily
#qpy:fullscreen
#qpy://0.0.0.0:9999/
"""
Mydaily-Android
Author Shenlang
"""

import sys, sqlite3, os
from bottle import Bottle, route, abort, request, response, template, ServerAdapter
import time
import requests
import xml.etree.ElementTree as ET

reload(sys)
sys.setdefaultencoding('utf-8')

ROOT = os.path.dirname(os.path.abspath(__file__))
textTpl = """<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[%s]]></Content>
             </xml>"""


class MyWSGIRefServer(ServerAdapter):
    server = None

    def run(self, handler):
        from wsgiref.simple_server import make_server, WSGIRequestHandler
        if self.quiet:
            class QuietHandler(WSGIRequestHandler):
                def log_request(*args, **kw): pass
            self.options['handler_class'] = QuietHandler
        self.server = make_server(self.host, self.port, handler, **self.options)
        self.server.serve_forever()

    def stop(self):
        #sys.stderr.close()
        import threading 
        threading.Thread(target=self.server.shutdown).start() 
        #self.server.shutdown()
        self.server.server_close() 
        print "# QWEBAPPEND"


def insert_data(data):
    """insert data from input to Database
    """
    db = sqlite3.connect(ROOT+'/mydaily_data.db')
    c = db.cursor()
    c.execute('INSERT INTO mydaily_data VALUES (?,?,?)', data)
    db.commit()
    db.close() 



def fetch_data():
    """ fetch data from database
    """
    db = sqlite3.connect(ROOT+'/mydaily_data.db')
    c = db.cursor()
    c.execute('SELECT * FROM mydaily_data')
    b = c.fetchall()
    return b


def chech_login(username, password):
    if username == "xpgeng@126.com" and password =="123":
        return True
    else:
        return False
    

#def all_tags():
#    db = sqlite3.connect(ROOT+'/mydaily_data.db')
#    c = db.cursor()
#    c.execute('SELECT 'tag' FROM mydaily_data')
#    b = c.fetchall()
#    return b

#@app.route('/login')
#def login():
#    """use bootstrap to design a homepage
#    """
#    template_home = env.get_template('signin.tpl')
#    return template_home.render()

#@app.route('/login', method='POST')
#def do_login():
#    input_email = request.forms.get('email')
#    password = request.forms.get('password')
#    if chech_login(input_email, password):
#        response.status = 303
#        response.set_header('Location', '/mydaily')
#    else:
#        return "<p>Login failed.</p>"
app = Bottle()

@app.route('/')
@app.route('/mydaily')
def mydaily():
    """home page
    """
    return template(ROOT+'/index.html')
    

@app.route('/mydaily', method='POST')
def save_mydaily():
    """ receive input and show database content in the browser
    """ 
    content = request.forms.get('content')
    tag = request.forms.get('tag') 
    now = time.time()
    if content in ['r','h','c']:
        echostr = textTpl % ('server', 'phone', int(time.time()), content)
        r = requests.post('http://mydailywechat.sinaapp.com/', echostr)
        root = ET.fromstring(r.content)
        msg_dict = {}
        for child in root:
            msg_dict[child.tag] = child.text
        return template(ROOT+'/whole.html', content = msg_dict['Content'])
    #I didn't add the function of deleting some item    
    else:
        content_tag= ".%s#%s" %(content, tag)
        echostr = textTpl % ('server', 'phone', int(time.time()), content_tag)
        requests.post('http://mydailywechat.sinaapp.com/', echostr)
        data = now, content.decode('utf-8'), tag.decode('utf-8')
        insert_data(data)
        previous_content = fetch_data()
        return template(ROOT+'/template.html', rows=previous_content)


try:
    server = MyWSGIRefServer(host="0.0.0.0", port="9999")
    app.run(server=server,reloader=False)
except Exception,ex:
    print "Exception: %s" % repr(ex)

