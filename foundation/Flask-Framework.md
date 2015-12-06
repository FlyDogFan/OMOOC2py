#Flask Framework 学习笔记
##背景
- 在5w课的任务里, 小赖用flask框架重写了任务, 并且做出了非常好看的界面. 通过小赖了解到flask第三方库非常多, 而且学习成本很低, 所以决定尝试用flask framework 开发web.
- 具体的安装教程这里就不介绍了, 可以参考[官方文档](http://flask.pocoo.org/docs/0.10/installation/)
- 这里主要记录一些我个人认为对于今后的开发非常有用的功能.



##功能
### virtualenv解决的问题
- 开发过程中, 由于Python版本不同, 后者libraries版本不同, 这样导致兼容性出现问题.
- 使用virtualenv能够针对不同的项目, 建立绝地孤立的环境.
- 安装命令`sudo pip install virtualenv`
- 建立venv `virtualenv venv`
- 激活venv `. venv/bin/activate`
- 退出venv`deactivate`
- 注意: 之所这么做的原因是, 每次开发我们就可以针对该项目下载所需要的第三方库, 库文件都存放在venv中. 这样不会影响系统python的库内容.
        
        问题在用vertualenv重写5w的任务过程中, 使用dev_server.py调试, 结果总是提示错误: no module named flask. 可是我明明已经安装好了.  
        原因:dev_server.py运行的时候应该不在这个虚拟环境里, 而系统环境我是没有装flask的. 所以无法调用到flask. 我退出环境, 在系统环境下安装好flask就没有了这个问题.
        查看文件权限的命令: $ls -l
         
       
###Static files
- 怎么用?
- 




固定地方.
交流+止损时间.