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
    r = requests.get('http://localhost:8080/client')
    print r.content

if __name__ == '__main__':
    main()