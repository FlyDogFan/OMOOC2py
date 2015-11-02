#Mydaily Version 3.0

##背景

    系统：OS X 10.11
    python版本:2.7.10
    编辑器：Sublime Text 3
    终端：iterm2


Mydaily已经更新到了version 3.0,也逐步从本地Terminal到本地GUI界面, 再到目前的内网版本.  
主要用到的基本知识有:  

- 理解什么是[UDP协议](https://en.wikipedia.org/wiki/User_Datagram_Protocol)  
- [Python库中关于socket的一些函数](https://docs.python.org/2.7/library/socket.html)
- while语句
- if语句

##使用
- 开启两个的Terminal, 多端就开启多个Terminal
- 先运行sever.py
- 再运行client.py
- 在client端输入文本即可发送到server端,并保存记录.
- 在client端输入`pre`查看历史记录

## Socket必备知识
###端口
- 信息传输需要的信息: IP, 端口号PORT
   - 端口号和进程是一一对应的.
- PORT + IP = unique网络进程
- 端口号范围: 0~65535
   - 0~1023 周知的端口
   - 1024~65535 用户自定义
- 半相关表示: 协议, 本地地址, 本地端口
- 完整描述: 协议, 本地地址, 本地端口, 远程地址, 远程端口


###调用方式
 `socket.SOCK_XXXX`
 
 - SOCK_DGRAM
    - 数据报socket, 用于[DUP通信]()
    - 无连接的服务?
    - 报文传输是无序的, 不可靠.

##coding过程
###建立sever与client的连接.
- 基于前一次经验, 发现上来就沉迷到看文档里, 实在是与"最小代价解决问题"相违背. 于是果断Google一下有没有相应的带例子的文档.在实例中明白了自己要用的一些函数的意义, 以及一些必要知识, 然后参考官方文档中的解释, 进一步理解其中的机制.
- 同时还发现不同的协议所用的语法也不相同.
   - 比如socket.listen()在UDP协议中就使用不了.
   - 具体的区别待版本完成后会仔细分析.
- 于是最初级的代码如下  

```python  
# _*_ coding:utf-8 _*_
#! /usr/bin/env python
'''
server
'''
import socket  
  
address = ('127.0.0.1', 31500)  
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
s.bind(address)  
  
while True:  
    data, addr = s.recvfrom(2048)  
    if not data:  
        print "client has exist"  
        break  
    print "received:", data, "from", addr  
  
s.close()  
``` 
- 其中的`while True:`保证了server端可以一直开启接受client端的连接.

```python
# _*_ coding:utf-8 _*_
#! /usr/bin/env python
'''
client
'''
import socket  
  
address = ('127.0.0.1', 31500)  
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
  
while True:  
    msg = raw_input()  
    if not msg:  
        break  
    s.sendto(msg, address)  
  
s.close()
```
###server端保存文件
- 定义一个保存文本的函数

```
from datetime import date

def save(data):
    with open('dairy.md','a') as f:
	    now = date.today()
	    f.writelines("%s\n\n%s\n\n"%(now,data)) 
	    
```
- 嵌入到server的脚本中, 使得在输出client输入的文本的同时, 保存到md文件中.

###获得历史消息
- 思路
   - client端接受输入并传递给server
   - 同时,判断输入的字符
   - 如果为"pre", 则执行接收命令
   - server端接受指令
   - 判定指令, 如果为"pre", 
   - 执行读取文档内容,发送内容到client端.
   - 在client显示server储存的内容.
- 代码

```python
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

``` 
```python
# _*_ coding:utf-8 _*_
#! /usr/bin/env python
'''
客户端
'''
import socket  
def main():

    BUF_SIZE=1024  
    server_address = ('127.0.0.1', 7777)  
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
```

- Debug
   - client端输出"pre"后, 连同"pre"也一同跟着输出.
      - 解决办法: 将读取server端文档内容的函数, 与保存输入端文档内容的函数分开运行.

   - > File "/Users/xpgeng/Anaconda/anaconda/lib/python2.7/socket.py",        
     > line 228, in meth  
     > return getattr(self._sock,name)(*args)
socket.error: [Errno 48] Address already in use  

       - 这是一个端口占用的问题.改了端口就可以解决.
       - 同时可以用一下命令,查看什么进程在占用什么端口.
        
          > $ ps -fA | grep python 
       
       - 用`$ kill  端口号` 即可杀死进程.
       - 还可以用如下命令, 确定sever的端口
          > $ python -m SimpleHTTPServer 8910
###


##Idea
- GUI下如何进行通信?
- 是否能读取指定日期的记录?
   - 这个如果解决了会很有意思.

##更新
151102  编辑 
