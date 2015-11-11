#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sqlite3

#reload(sys)
#sys.setdefaultencoding('utf-8')

db = sqlite3.connect('mydaily_data.db')
db.execute('''CREATE TABLE mydaily_data (time text ,diary_content text)''')
db.execute("INSERT INTO mydaily_data VALUES ('2015-11-10','hello world!')")
db.execute("INSERT INTO mydaily_data VALUES ('2015-11-10','hello world!!')")
db.execute("INSERT INTO mydaily_data VALUES ('2015-11-10','hello world!!!')")
db.execute("INSERT INTO mydaily_data VALUES ('2015-11-10','中文')")
db.commit()
db.close()
