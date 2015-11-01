# _*_ coding:utf-8 _*_
#! /usr/bin/env python
'''
server

'''
import socket  
from datetime import date

def save(data):
    with open('diary.md','a') as f:
	    now = date.today()
	    f.writelines("%s\n\n%s\n\n"%(now,data)) 

def read_diary():
    with open('diary.md','r') as f:
        return f.read()
def main():
    BUF_SIZE = 1024  
    server_address = ('127.0.0.1', 7777)  
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    server.bind(server_address)  
  
    while True: #可以保证server端连续运行 
        data, client_address = server.recvfrom(BUF_SIZE)  
        if not data:  
            print "client has exist"  
            break  
        elif data == "pre":        
            message = read_diary()
            server.sendto(message, client_address)    
        else :
            save(data)
            print "received:", data, "from", client_address    
    server.close()

if __name__=="__main__":
    main()  