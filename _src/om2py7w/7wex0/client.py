#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mydaily-web-client
Author Shenlang

"""

import sys,requests

reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    print """
	      HELP:
          'pre' : 打印所有日记
          'q' ,'quit': 退出
          'tag': 按标签查询日记
          'da': 清空数据库
	      """

    input_content = raw_input('> ')
    
    if input_content == "tag":
    	r2 = requests.post('http://localhost:8080/mydaily/client', 
        	                data = {tag_input})
    	tag_input = raw_input('Please write your tag > ')
        r2 = requests.post('http://localhost:8080/mydaily/client', 
        	                tag = {tag_input})
    else:
    	r3 = requests.post('http://localhost:8080/mydaily/client', 
        	                data = {input_content})
    r = requests.get('http://localhost:8080/mydaily/client')
    print r.content

if __name__ == '__main__':
    main()