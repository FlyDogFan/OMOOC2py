#Mydaily-Web 指北

##背景
- 当我们通过前几周循序渐进的学习, 学会了用Terminal进行内网的日记交互, 可是问题来了, 我们不能总无时无刻的带着client.py吧. 然后某一天一摸兜, 我发现忘记带了U盘, 登录邮箱下载吧, 可是这又是内网, 没法下载. 这时候, 我们的需求就来了: Mydaily-Web版!
- 背景:
      
      > System: OS X 10.11  
      > Terminal: Iterm2 + Tmux   
      > Editor: Sublime  
 
##功能需求
- 通过网页访问系统:
     - 每次运行时合理的打印出过往的所有笔记
     - 一次接收输入一行笔记
     - 在服务端保存为文件
- 同时兼容 3w 的 Net 版本的命令行界面进行交互

##知识准备
- Web Framework
   - 我的理解是, Framework就是一个平台, 它提供一些基础的函数, 比如,接收,发送,新建一个web页面, 给这个页面配备一个地址等等. 现在这个页面上什么都没有, 于是我们可以根据自己的开发需要去添加各种模块, 丰富这个页面.  
- Template
   - 我的理解是, 模板相当于解释器, 通过写入模板可识别的语句, 可以将我们对页面的各种布局, 文本处理等等都转化为框架所接受的命令.
   - 目前常用的模板有Django, Flask 
- Database


##功能分解
### 网页输入 
- 在Bottle提供的用户名+密码的example的基础上做些更改即可实现简单的网页输入.
- 代码如下:

```
@route('/mydaily')
def mydaily():
	return '''
	    <form action="/mydaily" method="post">
日记: <input content ="content" type="text" />
<input value ="保存" type="submit" />
      </form>
      '''	 

@route('/mydaily', method='POST')
def receive_and_save_mydaily():
	daily_content = request.forms.get('content')
	print "srv.got:", daily_content
	if daily_content:
		return template("<p>Done!<hr/>{{ name }}<p>"
		        , name= daily_content)
```
- 效果图:  
![mydaily-1](http://7xnwxz.com1.z0.glb.clouddn.com/mydaily-1.png)  
![input-1](http://7xnwxz.com1.z0.glb.clouddn.com/input-1.png)

- 这里要明白route, 也就是`路由`的概念. 同一个页面, 方法(method)不同, 可是同时实现不同功能. 同一功能也可以添加多个路由.

###保存输入
- 首先尝试的是以前的路子, 得到输入信息, 然后`open()`等等一套下去, 直接将输入保存为文本.
   - 这里遇到了一个坑, 就是需要重启web server, 修改才会生效.
- 后来又尝试使用数据库.
   - 首先要建立一个数据库.
       - 具体可以参考[官方文档](https://docs.python.org/2/library/sqlite3.html#module-sqlite3)
       - [这里]()是建立数据库的脚本. 
   - 将输入写入到Database中.
       - 这里遇到问题: 无法输入中文.
           - 问题肯定是出在编码上了. 可是搜了之后都是让转码.可是我已经各处都设定了编码为utf-8.为什么还要转码? 
           - 转完之后还要解码.解码的时候list 又用不了.!!! 
           - 在insert数据的时候加上`decode(utf-8)`, 就可以输入中文.
   - 我将写出数据库写成了一个函数

   ```
   def insert_data(data):
    """insert data from input to Database
    """
    db = sqlite3.connect('mydaily_data.db')
    c = db.cursor()
    c.execute('INSERT INTO mydaily_data VALUES (?,?)', data)
    db.commit()
    db.close()
    ```
       - 注意`db.commit()`非常重要, 因为这句是为了保存写入的.如果没有, 你就会发现, 在网页上每次输入都是在覆盖前一次输入...我就进了这个坑我会说么..  

###加入Jiaja2模板
- 添加模板步骤如下
    - 导入模板, 创建模板环境
    
      > template_loader = FileSystemLoader('views')  
      > env = Environment(loader=template_loader)
 
      - 其中`views`为存放模板的文件夹, 可以用绝对路径.

    - 加载模板, 并给模板中的变量赋值.
      
      > template_2 = env.get_template('template.tpl')  
      > return template_2.render(rows=previous_content) 
      
- 模板的样式写法自行Google, 这里就不细说了.


###显示过去内容
- 首先是读取数据库的信息, 并且修改成输出的样式, 比如添加`:`之类的.
  - 这里我定义了一个函数`fetch_data()`, 这样直接调用就好.
  
   ```python
   def fetch_data():
    """fetch data from database
       add ':' between every item
    """
        db = sqlite3.connect('mydaily_data.db')
        c = db.cursor()
        c.execute('SELECT * FROM mydaily_data')
        b = c.fetchall()
        d = []
        for member in b:
            a = "%s : %s\n"% member
            d.append(a)
        return d 
        db.close() 
    ```   
- 输出到模板
  
  ```python
  previous_content = fetch_data()       
  template_2 = env.get_template('template.tpl')
  return template_2.render(rows=previous_content)
  ```    
  - 耗了很久才输出到网页上. 数据库读出来的数据没法在模板中用for-loop输出出来.
  - 然后就在我觉得要及时止损的时候,, 通了....
  
      ![](http://7xnwxz.com1.z0.glb.clouddn.com/mydaily-web.png)
       

###兼容命令行交互
- 这一功能主要是通过`websocket`这一module来实现的.
   - 首先是server端的地址要改写成使用websocket的代码.如下
   
   ```
   from gevent.pywsgi import WSGIServer
   from geventwebsocket import WebSocketError
   from geventwebsocket.handler import WebSocketHandler

    server = WSGIServer(("localhost", 8080), app,
                    handler_class=WebSocketHandler)

    server.serve_forever()
   ```
   
   - 学习了小赖的处理方式, 重新开一个路由, 来负责命令行交互接受与发送.
   
    ```python
    @app.route('/client')
    def client():  
    """This is designed for terminal interaction.
    """  
    wsock = request.environ.get('wsgi.websocket')
    if not wsock:
        abort(400, 'Expected WebSocket request.')
    while True:
        try:
            message = wsock.receive()
            if message == "pre":
            	previous_content = only_fetch_data()
                wsock.send(previous_content)
                sleep(3)
                wsock.send(previous_content)
        except WebSocketError:
            break
    ```    
   - client端要先安装`websocket-client`这个module才可以运行.
  
        > pip install websocket-client
        
      - 如果提示不允许安装, 果断用`sudo`安装.
   
   
   ```
   from websocket import create_connection

   ws = create_connection("ws://localhost:8080/client")
   msg = raw_input('> ')
   ws.send(msg)

   print "Receiving..."
   result =  ws.recv() 
   print result

   ws.close()

   ```
   
   - 目前还有一个问题没有解决了.
      - server端返回的历史数据到client端接受的时候, 全变成了`str`, 所以导致读出来的数据都是编码且不是成条的, 而是每个字符为单位的.
      - 还在debuging!


##感想
 - 遇到问题, 解决问题, 是有快感的.
 - 在coding的过程中, 不时的参考下style guide, 每天掌握一点其中的内容, 长期下来, 代码风格肯定会有很大改观.
 - 直觉上没那么难的东西, 会卡一定的时间, 但往往突破也就在一瞬间.
 - 善用`print`, 什么东西模糊不清楚, print一下, 看看变量数, 每一步传递都是什么东西, tuple长什么样.



##References
- <http://bottlepy.org/docs/dev/index.html>
    - Bottle的官方文档  
- <http://jinja.pocoo.org/>
    - Jinja2的官方文档 
- <https://docs.python.org/2.7/library/sqlite3.html>
   - sqlite3的官方文档.  
- *<https://www.jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/>
   - 系统的介绍了web framework 
- <https://en.wikipedia.org/wiki/Web_application_framework>
- <http://stackoverflow.com/questions/10316374/bottle-websocket>
- <https://websockets.readthedocs.org/en/latest/api.html>
   - websocket的官方文档.   