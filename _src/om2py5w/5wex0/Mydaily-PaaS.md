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

      >$ touch index.php  
       $ git add index.php  
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
     - [代码](https://github.com/xpgeng/mydaily-paas/tree/97b5ae72e86316239548df0a2a9db9f2c63ef671)


###Client.py
- 与上周类似, 只是链接修改成SAE提供的链接即可.
- 这里要感谢小赖告诉我的一个用法

  > content = '\n'.join([row[0]+'>>'+row[1] for row in previous_content])
  
  - 真不知道还可以这么写!

- [代码](https://github.com/xpgeng/OMOOC2py/commit/a54eb44082a69f1286042a3ceeffef783bfe16d3)


###



##Review
- 大部分时间都花在了配置上, 所以会有很沮丧的感觉. 时间没少花, 但是没有什么产出.
- Debug的速度很慢, 还是不能做到遇到问题, 能马上进行正中靶心的搜索, 迅速找到解决方案.
 


##References
- [PaaS-Wiki](https://en.wikipedia.org/wiki/Platform_as_a_service)
- [SAE官方文档](http://www.sinacloud.com/doc/sae/python/index.html)
- [SAE-git配置](http://www.sinacloud.com/doc/sae/tutorial/code-deploy.html)
- [SAE-KVDB官方手册](http://www.sinacloud.com/doc/sae/python/kvdb.html)