#Mydaily-Web

##Introdution
这个一个极简日记交互工具的网页版. 通过在内网中访问网址, 即可记录日记, 同时查看历史输入. 
##Example

![example](http://7xnwxz.com1.z0.glb.clouddn.com/mydaily-web-example.png)

##Motivation
开发这个工具是为了方便我们在内网中, 随时随地, 任意电脑, 无需安装即可记录我们此时此刻的想法.

##Installaion
- 下载文件. 
     - server.py
     - client.py
     - folder:views 
     - bottle.py
     - create_database.py
     - 以上都在[这里](https://github.com/xpgeng/OMOOC2py/tree/master/_src/om2py4w/4wex0)

- 安装modules.`pip install Module_Name`
     - websocket
     - websocket-client
     - gevent
     - Jinja2
     - gevent-websocket
- 运行`create_database.py`生成数据库.
- 运行server.py.
- 浏览器端输入:`http://localhost:8080/mydaily`
     - 输入日记
- 运行client.py.
     - 输入`pre`查看历史记录.

##Author
- 沈浪
- [Gitbook](https://www.gitbook.com/book/xpgeng/omooc2py/)
- [Github](https://github.com/xpgeng)
- Email: shenlang.zyxyz@gmail.com

##Copyright
 Mydaily-Web is released under the MIT License.

##Bugs
- 目前client端得到的输入还是乱码. 正在修理ing.
       
