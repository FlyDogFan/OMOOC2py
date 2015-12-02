# -*- coding: utf-8 -*-
#qpy:webapp:Mydaily
#qpy:fullscreen
#qpy://127.0.0.1:8080/
"""
Mydaily-Android
Author Shenlang
"""

import sys, sqlite3, os
from bottle import Bottle, route, abort, request, response, template, ServerAdapter
from datetime import date

reload(sys)
sys.setdefaultencoding('utf-8')

ROOT = os.path.dirname(os.path.abspath(__file__))


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
    daily_content = request.forms.get('content')
    tag = request.forms.get('tag')
    now = date.today()
    #print "srv.got:", data
    if daily_content:
        data = now, daily_content.decode("utf-8"),tag.decode("utf-8")
        insert_data(data)
        previous_content = fetch_data()
        return template(ROOT+'/template.html', rows=previous_content)


@app.route('/client')
def client():
    """This is designed for terminal interaction.
    """
    content = ''
    db = sqlite3.connect('mydaily_data.db')
    c = db.cursor()
    c.execute('SELECT * FROM mydaily_data;')
    content = '\n'.join([row[0]+':'+row[1] for row in c.fetchall()])# should be modified
    c.close()
    return content


try:
    server = MyWSGIRefServer(host="127.0.0.1", port="8080")
    app.run(server=server,reloader=False)
except Exception,ex:
    print "Exception: %s" % repr(ex)

