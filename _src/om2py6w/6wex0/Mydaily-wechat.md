#Mydaily-Wechat
##背景
- 利用公众号提供后台开发API, 将上周的极简日记WEB版修为微信后台, 使得我们通过微信公众号就可以完成极简日记交互.

    > 系统  Mac OS X 10.11  
    > Terminal: iTerm2+Tmux  
    > Platform1: Wechat  
    > Platforn2: SAE   
 
##任务分解
###服务器配置
- 在SAE上建立服务器.
   - 设置好二级应用名称, 应用描述等等. 
- 本地新建关于Mydaily-wechat的一个文件夹. 为了方便管理, 我们统一在`Project`下建立各种项目的文件夹.
   
   > mkdir Project  
   > mkdir mydaily-wechat
   
- 初始化仓库, 并与sae建立好的应用相连接.
    >$ git init    
    >$ git remote add `sae` https://git.sinacloud.com/`App_Name`
       - 注意是二级应用名称.可以在应用设置里看到.
       - `sae`可以替换成你任务不容易欢笑的名称, 比如我就改成了`mwechat`.
 
- 新建`config.yaml`,内容如下

    > \---     
      name: App_name   
      version: 1  
   - 注意,千万不要有多余的空格,格式错误等, 之前在这就遇到过坑. 调试起来都找不到原因.

- 新建index.wsgi.
   - 这是重头戏, 验证token的整个配置代码都在这里完成.
   - 这是微信关于配置的[官方文档](http://mp.weixin.qq.com/wiki/16/1e87586a83e0e121cc3e808014375b74.html#)
   - 具体这里需要包含的内容有
       1. web框架--我们选择bottle
       2. token(我们自己设置好的)
       3. hashlib module(由官方文档知道, 需要用到sha1加密)
   - 代码在[这里]()
   - 其中这里用到的函数有 `.sort()`排序, `hashlib`中的加密函数`.sha1`, 获取16进制字符串`.hexdigest()`
   - 配置好后, Push到remote repo.

- 在微信的配置界面输入设置好的token, 按要求提交即可.
- 至此, 接头工作已经完成. 接下来就要进行相关开发工作.
      
###消息响应
1. 最基本功能, 即: 用户输入任何字符, 返回一条欢迎语.
   - 因为不知道sae上返回什么数据是微信可以接受的, 所以直接搜索了一些例子, 从例子中找到答案.
   - 第一种方案是在`index.wsgi`中写一个模板, 然后把用户, 开发者, 以及时间, 想要说的话替换掉模板的变量, 然后返回模板给微信.
   - [代码](https://github.com/xpgeng/OMOOC2py/commit/7d03b31b35b267051798fff2f2f4e342886fda65)
   - 第二种方案是把xml模板单独写一个文件, 然后在主模块中调用这个模板, 我觉得这种方式很好, 但是尝试了用`jinja2`去调用, 但目前失败.我分析的原因是xml文件中的变量格式是不是jinja2调用的时候,识别不了. 因为这个并不是特别重要, 只是方式上感觉更优雅. 所以没有进一步探索. 有时间会回过头来修改.
  
2. 添加事件驱动回复. 即: 关注后, 立即返回欢迎模板.
   - 这里要注意, 被关注后, 微信发来的xml模板中, MsgType == 'event', 返回给微信的xml模板需要的是"text", 我在这调试了两次才意识到这个问题. 之前都是一直在用 msg_dict['MsgType'].
   - [代码](https://github.com/xpgeng/OMOOC2py/blob/4703fc933311069c432948edc9b8888a4aba7be3/_src/om2py6w/6wex0/index.wsgi)
   - 注意: 这里给出的代码都是在当前过程中push到repo的版本, 并不是最终版本的截取, 这对于逐步了解每一个功能的实现非常有帮助.

3. 将用户输入的内容保存到数据库, 同时可以随时调出过去的输入.
   - 这里苦恼的是如何debug, 因为我们不可能改一点, 然后push一下, 然后看看微信什么反应, 这样很麻烦. 通过大妈的演示, 可以设计一个client端, 模仿微信的输入, 同时得到sever端返回的信息. 不用要求完备可用, 只需要能帮助我们迅速错误出现在什么地方就好.
   - 仿照大妈的演示, 通过判断输入的字符来确定接下来的执行的命令.
   - debug过程, 不断打印出自己想看见的变量, 真的非常方便.
   - 读取数据库的时候用到了新学到的`.join(for ...in...)`
   - [代码](https://github.com/xpgeng/OMOOC2py/commit/97d974df874071a0ad310546a33826e611de46e0) 
 

###指令设计
- `.+输入内容`: 输入笔记
- `r`:阅读过去输入
- `h`:帮助
- 添加标签.
   - 通过判断字符是不是`#`, 然后截取标签, 返回标签值的同时, 返回读取的数, 方便下一步截取真正的输入内容.
- `d+数字`:删除指定条目. 
-  'c':clear all.
- [代码](https://github.com/xpgeng/OMOOC2py/commit/de360f820a5c2e19f9ad17fa94d66802f0e37ea9)

###client端
- 通过client端同样能够输入笔记, 同时完成上述设计指令.
- 其中遇到的坑:
   - 在脚本中即用了`requests.post`又用了`requests.get`
   - 然后再不断debug中发现, `get`没有起到任何作用.
   - 
- [代码](https://github.com/xpgeng/OMOOC2py/commit/1c8f2543e86665046dc4d26735fc008fc7ffcd30)
- 注意: 使用时将Client.py中的连接修改能公网连接.
###目前还未完善的功能
- 加密
- 识别用户来源
- 分用户储存数据

> 以上的功能会在Daily-Review中实现.


##思考
- 微信端可不可以跟web端兼容? 慢慢实现类似全平台的效果. 
- 对课程一点小感受
   - 任务的进化是永无止境的, 除了完成任务, 呈现出自己的想法, 作品以外
   - 更关键的是发现自己的姿势对不对, 什么地方不对, 该怎么改进, 已经做了什么努力, 有了什么效果, 仍有什么不足, 该怎么改进,已经做了什么努力, 有了什么效果, 仍有什么不足...
- 现在对于debug, 变得乐在其中
   - 针对出现错误, 迅速锁定该行, 输出一下看看结果, 然后修改
   - 如果该错误实在找不到解决方案, 马上进行搜索
   - 如果搜索结果不理想, 马上去寻找折中方案, 先能过了这坎再说
   - 记录没能解决的问题, 带任务结束后回顾过程中再慢下来思考到底是什么原因.
- 代码还不够易读. 希望未来重构的时候可以改进.
    
##更新
151124  编辑



##References
- <https://docs.python.org/2.7/library/xml.etree.elementtree.html>
   - 关于XML的Python官方库. 其中提供了一些函数如何读取,提取XML文件中的各种信息. 
- [Wechat-接收普通消息](http://mp.weixin.qq.com/wiki/17/fc9a27730e07b9126144d9c96eaf51f9.html)
- [Wechat-接收事件推送](http://mp.weixin.qq.com/wiki/14/f79bdec63116f376113937e173652ba2.html)
- [Wechat-被动回复用户消息](http://mp.weixin.qq.com/wiki/18/c66a9f0b5aa952346e46dc39de20f672.html)
- [KVDB](http://www.sinacloud.com/doc/sae/python/kvdb.html)
- <http://my.oschina.net/yangyanxing/blog/159215>