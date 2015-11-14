# _*_ coding:utf-8 _*_
#! /usr/bin/env python
"""
client
改用requests
"""
import requests


def main():
    r = requests.get('http://localhost:8080/client')
    print r.content

if __name__ == '__main__':
	main()
