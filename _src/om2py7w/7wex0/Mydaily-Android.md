#Mydaily-Android
##背景
像大妈所说, 终于期待的Android版本来了.

之前总觉得Android或者iOS开发就像神秘森林, 不知道里面有什么, 远远看去烟雾缭绕甚是迷人, 然后又总觉烟雾背后竟是悬崖峭壁.

于是在这样的心情下开始了这周的开发任务. 
 
        系统: Mac OSX 10.11
        Terminal:  iTerm2
        Editor: Sublime Text
        Mobilephone:  Mi3
        Script engine: Qpython
        

##功能
- [x] 在手机端每次接收一行的文本(不包含表情/图片/声音/视频...)
- [x] 使用专用指令,可打印出过往所有笔记
- [x] 在服务端合理存储/管理
- [x] 同时兼容:
   - [x] 命令行工具
   - [x] 微信公众号



##过程
### 安装Mirrorop, 将手机屏幕投到电脑中, 以便调试.
   - 软件[下载地址](http://www.mirrorop.com/product_mac_Receiver.html)
   - 手机下载sender文件, 电脑安装receiver文件.
   - 之前分错了sender和receiver... 这种坑真的是不踩也罢. 好伤啊...!!
   - 更伤的是现在发现, 根本用不到啊. 这功能跟调试完全没有关系啊...T_T...哭晕在厕所.

###修改4w任务代码, 使之能够运行在手机端.
   - 使用了module:`sqlite3`
   - 首次在手机端连首页都loading不出来, 怀疑是4w用的server调用了gevent这个包, 在电脑上是后来才安装这个包的, 所以, Qpython应该没有这个包, 所以参照bushelper的server代码, 修改了main.py的server代码. 
        - 现在回过头来看过程, 其实是可以用`pip`命令来安装`gevent`包的. 
   - 再次不成功, 不过这次提示的是template不能调用.
   - 再次看BusHelper的代码, 发现他使用的是绝对路径, 所以继续修改该代码, 加入绝对路径.
   - 这次终于能够显示了. ;-)
   - [代码](https://github.com/xpgeng/OMOOC2py/commit/3f84a0f53e2f6bea6a7b607c09c9ea4ed9d7c37d#diff-90a244f7292321d7fd567f962f65eb34)

###添加Tag, 修改Database
   - 只需要在生成Database的脚本里做修改, 多添加一列"tag"
   - 同时修改main.py和template. 因为此时写入和读取数据库, 都变成了三列: "time", "content", "tag".
   - [代码](https://github.com/xpgeng/OMOOC2py/commit/756bd849673c2d74f75fb84d18181d9a841a9c43) 
    
###连接SAE
   - 我的理解是, 完全可以将手机端当做是SAEserver端的一个client端. 只不过是这个client端带有自己的模板, 能将请求的的数据显示在手机页面而已. 按着这样的理解, 我只需要将之前几周任务的client端代码补充进main.py即可.
   - 需要`requests`库.
      - 因为是要在手机上运行, 所以还要在Qpython里下载这个库.
      - 打开Qpython, 在库里点击`pip console`就可以用`pip`安装相应的库.
      - 此处出现了目前最大的坑, 就是明明已经安装了requests库, 可是Qpython确调用不了.
      - 而且, 一开始只是显示`Error: web app lauch timeout(10)`, 并不知道错误出在哪里.
      - 后来才发现Qpython会返回一个日志, 上边记录了错误信息.
      - 所以现在尝试正确安装上requests. 如果不行, 就准备换姿势.
      - 反复安装不成功, 然后卸载了Qpython,重新安装`requests`
      - Done! 
   - 因为考虑到要跟微信兼容, 又为了偷懒;-),,,我看大家偷懒的时候都打着`最小代价`的旗号...所以决定使用XML格式传输信息.
   - 同时又增加一个template, 用来显示SAE数据库中的全部内容.
   - 这样, 只要仿照微信的交互口令, 就可以完成简单的手机端交互.
   - [代码](https://github.com/xpgeng/OMOOC2py/commit/69f5474f4cddb38921cf016fca37f2319988dfbd)
   
    ![](http://7xnwxz.com1.z0.glb.clouddn.com/mydaily-android.jpg)
   
      - 注意图片中的时间, 因为使用了`time stamp`, 还未转化成标准时间格式.
      - 关于time, 其实有很多东西可以挖, 可以看看我最近整理的一篇关于time的[文章](https://xpgeng.gitbooks.io/omooc2py/content/foundation/Module-time.html)

###界面美化(未完成)

##Debug
- 目前输出的格式还比较粗糙, 待修改.

##体会
- 这次又在配置上浪费了一些时间. 我自己的感觉是, 一涉及到配置, 有些时候如果教程不够详细, 很容易就走到坑里. 而且在配置过程中, 会觉得很简单, 导致某些地方看的不够仔细, 也很容易掉坑.
- 就web app而言, 用python开发非常便捷, 如果熟练可以迅速开发出一款应用的雏形.
- 这回又体会到了日志的重要, 不看日志, 根本不知道错误在哪. 都是自己瞎猜. 尤其Qpython只要出错, 后台都会有个日志提供了. 所以因为不看日志, 导致自己瞎猜好长时间错误出在哪. 一看日志马上明白了!!!



##更新
151129  编辑  
151201  更新  
151202  更新 sae  
151203  更新 添加`requests` 

##References
- [Qpython](http://qpython.org/)
- [Bottle-templates](http://bottlepy.org/docs/dev/tutorial.html#templates)
- [sqlite3](https://docs.python.org/2/library/sqlite3.html)





