#!/usr/bin/env python
# -*- coding: utf-8 -*-



import sys, sqlite3
from datetime import date

reload(sys)
sys.setdefaultencoding('utf-8')


db = sqlite3.connect('mydaily_data.db')
c = db.cursor()
now = date.today()
daily_content = "中文"
data = now, daily_content.decode('utf8')
c.execute('INSERT INTO mydaily_data VALUES (?,?)', data)
c.execute('SELECT * FROM mydaily_data')
previous_content = c.fetchall()
print previous_content#.encode('utf8')

