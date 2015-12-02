#Mydaily-Android
##背景


- Tools
     
         Mirrorop
         
     
  

##功能
    - 在手机端每次接收一行的文本(不包含表情/图片/声音/视频...)
    - 使用专用指令,可打印出过往所有笔记
    - 在服务端合理存储/管理
    - 同时兼容:
        - 命令行工具
        - 微信公众号


##过程
- 安装Mirrorop, 将手机屏幕投到电脑中, 以便调试.
   - 软件[下载地址](http://www.mirrorop.com/product_mac_Receiver.html)
   - 手机下载sender文件, 电脑安装receiver文件.
   - 之前分错了sender和receiver... 这种坑真的是不踩也罢. 好伤啊...!!
   - 更伤的是现在发现, 根本用不到啊. 这功能跟调试完全没有关系啊...T_T...哭晕在厕所.

- 修改4w任务代码, 使之能够运行在手机端.
   - 使用了module:`sqlite3`
   - 首次在手机端连首页都loading不出来, 怀疑是4w用的server调用了gevent这个包, 在电脑上是后来才安装这个包的, 所以, Qpython应该没有这个包, 所以参照bushelper的server代码, 修改了main.py的server代码. 
   - 再次不成功, 不过这次提示的是template不能调用.
   - 再次看BusHelper的代码, 发现他使用的是绝对路径, 所以继续修改该代码, 加入绝对路径.
   - 这次终于能够显示了. ;-)
   - [代码](https://github.com/xpgeng/OMOOC2py/commit/3f84a0f53e2f6bea6a7b607c09c9ea4ed9d7c37d#diff-90a244f7292321d7fd567f962f65eb34)

-  

##体会



##更新

##References