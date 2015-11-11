#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is used for debug Chinese Character input.
通过这个Script, 也可以学习到如何用sqlite3对数据库进行操作.
"""

import sys, sqlite3
from datetime import date

reload(sys)
sys.setdefaultencoding('utf-8')


db = sqlite3.connect('mydaily_data.db')
#db.row_factory = sqlite3.Row
c = db.cursor()
now = date.today()
daily_content = "中文"
data = now, daily_content.decode("utf-8")
#c.execute('INSERT INTO mydaily_data VALUES (?,?)', data)
db.commit()
c.execute('SELECT * FROM mydaily_data')
previous_content = c.fetchall()
#print len(previous_content)
#for row in previous_content:
#    print row #.encode('utf8')
#print previous_content.keys()
#print previous_content['diary_content']
#print previous_content
for item in previous_content:
    print item
db.close()