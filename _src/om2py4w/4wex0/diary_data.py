#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sqlite3
db = sqlite3.connect('mydaily_data.db')
db.execute("CREATE TABLE mydaily_data (data text, diary text)")
db.execute("INSERT INTO mydaily_data VALUES ('2015-11-10','hello world!')")
db.execute("INSERT INTO mydaily_data VALUES ('2015-11-10','hello world!!')")
db.execute("INSERT INTO mydaily_data VALUES ('2015-11-10','hello world!!!')")
db.execute("INSERT INTO mydaily_data VALUES ('2015-11-10','hello world!!!!')")
db.commit()
