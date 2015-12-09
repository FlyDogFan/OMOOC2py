#Mydaily-PaaS

##Background
- 极简日记交互系统经历了一系列内网的开发, 虽然目前功能还十分简陋, 但是产品都是不断迭代才越变越好, 所以极简功能的日记交互系统也在这周放到了线上进行不断迭代.
- 在不了解SAE这类云平台前, 总以为应用的开发都要花重金买个服务器, 然后各种手续俱全, 才能在公网运行, 然后要各种维护什么的.
- 如果你也有类似的感受, 那么看了下边的教程, 一定会让你觉得, 原来把应用放到公网上运行也没那么难.

##Preparation
- 什么是PaaS
  - Platform as a Service.
  - 可以提供给用户进行各种应用开发,运行,维护等的云服务平台.
  - 简单来讲, 就是我们不用买服务器了, 连VPS都不用, 直接在云平台上建个账户, 上传自己的开发文件, 然后按着平台所能提供的服务进行各种配置, 云平台会自动解析这些文件和配置, 生成应用, 并提供一个访问网址, 当然, 我们也可以绑定私人域名.
- SAE
  - Sina App Engine.
  - 新浪云平台. 
  - 支持Python开发.

##Process

###新建app
- 新建应用
- 确定二级域名
- 确定开发语言:Python2.7

###配置本地开发环境
- Git
   - 创建一个新的Git仓库并且添加一个Git远程仓库sae，地址为：https://git.sinacloud.com/App_Name 。
   - 部署Git的主分支（master）的代码到SAE服务器上的版本1中

      >$ git add .   
       $ git commit -m"initial commit"  
       $ git push sae master:1  
       
   - 这样我们就配置好了Git.

- 本地调试环境
   - [安装教程](https://pypi.python.org/pypi/sae-python-dev/1.3.5)
   - 我在安装好了之后一直没法运行dev_server.py
   - 通过重新安装, 设置PATH, 可以运行dev_server.py, 但是一直提示`ComposerError:.....`
   - 因为平台是国内的关系, 搜索的结果也不理想.
   - 后来都准备直接在线调试了. 但问题是在线调试根本不知道错误出在什么地方.
   - 后来又仔细搜索了一下, 发现是`config.yaml`中多写了三个`-`导致错误,所以本地环境一直不成功!
  

###使用Bottle框架
- 配置index.wsgi
   - 根据SAE提供的Bottle框架的例子, 修改了上周的代码.
   - 这版的[代码](https://github.com/xpgeng/mydaily-paas/tree/787075f203e3b5d3b857e5b01714e3cce6ebed88)


###添加数据库

- 添加KVDB
     - [SAE-KVDB官方手册](http://www.sinacloud.com/doc/sae/python/kvdb.html)
     - 我遇到了下面的问题.
     
     > MemcachedKeyCharacterError: Control characters not allowed
     
     - google 了一下, 虽然问题背景不同, 但看到有些问题的原因是空格引发的, 所以尝试将key也就是时间里的空格都删除, 好了!
     - 将数据保存到本地文件中
     
        > dev_server.py --kvdb-file=/Users/xpgeng/kvdb/local/kvdb.pkl
        
     - 注意: 这里要谢绝对路径! 
     - [代码](https://github.com/xpgeng/mydaily-paas/tree/97b5ae72e86316239548df0a2a9db9f2c63ef671)


###Client.py
- 与上周类似, 只是链接修改成SAE提供的链接即可.
- 这里要感谢小赖告诉我的一个用法

  > content = '\n'.join([row[0]+'>>'+row[1] for row in previous_content])
  
  - 真不知道还可以这么写!

- [代码](https://github.com/xpgeng/OMOOC2py/commit/a54eb44082a69f1286042a3ceeffef783bfe16d3)
- 因为功能的添加, 所以重写了client.py

###添加标签, 分类收集
- 目前能做到是, 添加tag框, 把key值对应成标签, 输入内容以及时间当做一部分存到value中.
- 但这样做的后果是tag为同一值时, 会覆盖之前写过的内容.
- 解决思路
   - 使用dict
   - 将同一标签下的日期与输入内容写成KV对, 同一放到同一标签下的字典中.
   - 在模板中应用for循环处理字典.
- 看到小赖的处理方法, 是把Key设为数字, 标签, 内容, 以及时间都统一写成字典放到Value中, 这显然比我的想法高级些.
- 之前看PPrint时候其实应该意识到可以这么写. 所以现在准备重新改写.
   - 首先是读取用户的标签, 内容, 
   - 写入KVDB. 写入的模板: {No.'数字'}, {time:strftime, content:BLABLBA, tag:XXXX}.
   - 计数.加入一条计数的KV对放到DB中.这样通过每次读取计数,+1, 就可以确定系统内多少条记录, 同时每条输入会有唯一的一个Key, 这样避免了倍覆盖. 之前我就经常发生覆盖的情况.
   - 按标签分类.同时对应每个标签, 都写入一条KV值, key为标签,  value对应No. 如果下一次输入出现相同标签, 我们就把输入条目对用的No.增加到该标签的value中.
- 这种方式是每个标签再设一个字典, 可是如果数据量增大的话, 在存储没有问题的情况下, 当然这种方法很简单, 但是每个人可能输入的标签的是不同的, 一万条不同, 就得多一万条标签. 这个时候是不是可以考虑用搜索但不储存的办法, 但搜索的弊端是要把数据遍历一边, 找到相同的标签, 如果数据量特别大的话, 遍历就很耗时间. 这时候就看存储和搜索时间哪个是更限制应用性能的条件.
- [代码](https://github.com/xpgeng/OMOOC2py/tree/master/_src/om2py5w/5wex0)
###美化模板
待完成





##Review
- 一部分时间都花在了配置上, 所以会有很沮丧的感觉. 时间没少花, 但是没有什么产出.
- 马上进行正中靶心的搜索, 迅速找到解决方案的能力还有待加强
- 进步的地方是debug的速度要比以前快很多, 出现问题, 截断print一下, 很快就能解决问题. 以前真是没养成不断print的好习惯!摔!
 
 


##References
- [PaaS-Wiki](https://en.wikipedia.org/wiki/Platform_as_a_service)
- [SAE官方文档](http://www.sinacloud.com/doc/sae/python/index.html)
- [SAE-git配置](http://www.sinacloud.com/doc/sae/tutorial/code-deploy.html)
- [SAE-KVDB官方手册](http://www.sinacloud.com/doc/sae/python/kvdb.html)
-  <http://blog.mattcrampton.com/post/31254835293/iterating-over-a-dict-in-a-jinja-template>