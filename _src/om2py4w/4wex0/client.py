# _*_ coding:utf-8 _*_
#! /usr/bin/env python
'''
客户端
'''
import socket  
def main():

    BUF_SIZE=1024  
    server_address = ('localhost', 8080)  
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
  
    while True:  
        message = raw_input('> ')  
        if not message:  
            break  
        client.sendto(message, server_address)  
    
        if message == 'pre':
    	    data = client.recv(BUF_SIZE)
    	    print data
    client.close()

if __name__=="__main__":
    main()  