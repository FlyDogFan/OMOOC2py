#Tmux 配置指北

##背景
- 为什么使用Tmux?
   - 当我们进行多Terminal开发project时, 不同的Terminal有不同的开发任务, 比如我在开发一个Web版的极简交互日记系统时, 一个负责处理server端, 一个要运行client脚本, 还要一个负责执行其他命令.
   - 这时候痛点就出现了, 我们在窗口间不停的切来切去, 很影响工作效率. 这时候聪明的同学会将窗口摆开,可是我们每天开始工作的时候, 第一件事就是摆窗口, 这岂不是很麻烦?
   - 所以, 我们选择用Tmux这样一个工具, 只需要几个口令, 就可以在同一个Terminal界面分成我们需要的各个窗口. 
- 照例

        系统: OS X 10.11
        Terminal: Iterm2
        Tmux版本: version 2.1
         

##什么是[Tmux](https://tmux.github.io/)
- "Terminal Multiplexer"的简称
- 简单来说, Terminal分窗工具. 一个窗口, 分成几部分, 可以让我们即编程, 又调试, 多端同窗口协同工作.
- 类似的工具还有dvtm, GNU Screen(1987发布第一版), splitvt等等.
- 这里推荐一个工具Byobu, 他默认Tmux为后端, 提供各种配置, 简直懒人福音.
- 想要熟练使用Tmux, 需要掌握Tmux各个模块的含义:
 
|server	|服务器|输入tmux命令时就开启了一个服务器|  
|---------|-----|------------------------------| 
|session	|会话|一个服务器可以包含多个会话|
|window	|窗口|一个会话可以包含多个窗口|
|pane	|面板|一个窗口可以包含多个面板|

 
##下载与安装
在 Mac OS 中安装：

   - 安装 Homebrew
    	
        ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

     有关安装 homebrew 的详细的信息可以参考这里。

   - 安装 Tmux
    
        $ brew install tmux

在 Ubuntu 中安装：

   - 在终端输入如下命令：

	    sudo apt-get install tmux
	    
W$呢? Sorry.....
##快捷键
要想熟练使用Tmux, 一定要熟记一些必要快捷键, 这里列出了大部分快捷键, 但并不是都要记住.
`C`= `Ctrl`

|tmux |开启|    sever   |
|---|------|:-----:||
| tmux ls| 显示已有tmux列表（C-b s）|session|
|tmux attach-session -t 数字| 选择tmux|session|
|tmux new -s session |建立会话|session|
|tmux new -s session -d|在后台建立会话 |session|
|tmux ls |列出会话| session|
|tmux attach -t session|进入某个会话| session|
|C+b s  | 现有会话列表|session|
|C+b c  | (creat)创建一个新的窗口|window|
|C+b n| (next)切换到下一个窗口|window|
|C+b p| (previous)切换到上一个窗口|window|
|C+b l| (last)最后一个窗口|window|
|C+b w |通过上下键选择当前窗口中打开的会话|window|
|C+b 数字 |直接跳到你按的数字所在的窗口|window|
|C+b &| 退出当前窗口|window|
|C+b d |临时断开会话 断开以后,还可以连上的哟:)|window|
|C+b " |上下划分|pane|
|C+b % |垂直划分|pane|
|C+b o |在小窗口中切换|pane|
|C+b  (方向键)| 在小窗口中切换|pane|
|Ctrl+b，不松开Ctrl，方向键 | 调整窗格大小|pane|
|C+b !| 关闭所有小窗口|pane|
|C+b x |关闭当前光标处的小窗口|pane|
|C+b t |钟表 |pane|
|C+b , |修改窗口名|pane|

注意: Tmux的快捷键开启都是先按`Ctrl`+`b`,放开后再按命令按键.


##配置
说实话, Tmux默认的快捷键操作起来十分不方便. 所以需要重新更改常用快捷键.

- 更改启动快捷键前缀`C+b`为`C+a`

  > \#remap prefix from 'C-b' to 'C-a'  
  > unbind C-b  
  > set -g prefix C-a  
  > bind-key C-a send-prefix

- 如果没有session,自动新建session
  > \#tmux attach 如果无分离终端则新建  
  > new-session
- 更改分屏快捷键

  > \# split panes using | and -  
  > bind | split-window -h  
  > bind - split-window -v  
  > unbind ' " '  
  > unbind %  

- 不同窗口间移动改成`Alt+ 箭头` 

  > \# switch panes using Alt-arrow without prefix  
  > bind -n M-Left select-pane -L  
  > bind -n M-Right select-pane -R  
  > bind -n M-Up select-pane -U  
  > bind -n M-Down select-pane -D  
  
- 用`C+a` + `r`更新配置, 使得无需重启就令配置及时生效

  >\# reload config file (change file location to your the tmux.conf you want to use)  
  > bind r source-file ~/.tmux.conf; display-message "Config reloaded.."

- 使用鼠标切换窗口

  > set-option -g mouse-select-pane on

如果每次打开Terminal都要重新为了习惯的布局各种快捷键撸一遍, 显然非常的不优雅, 于是我们有了下面的配置, 或者说脚本.

- 新建一个路径, 用来存储与Tmux 相关的各种文件
 
  > mkdir ~/.tmux
 
- 新建一个文件命名为`layout1`(根据未来project的不同, 可以有很多不同的layout)
  > nano ~/.tmux/layout1 
- 写入如下内容:
  > selectp -t 0 # select the first (0) pane  
  > splitw -h -p 50 # split it into two halves  
 
  > selectp -t 1 # select the new, second (1) pane    
  > splitw -v -p 50 # split it into two halves  
  > selectp -t 0 # go back to the first pane  
- 在`~/.tmux.conf`中再添加如下命令
  > bind D source-file ~/.tmux/layout1
- 用`C+a` +`r`更新下配置. 
- `C+a` + `D`就会出现如下界面.

  ![layout1](http://7xnwxz.com1.z0.glb.clouddn.com/layout1.png)

##日常使用
- 每次打开Terminal之后操作非常简单
    - 运行口令`tmux`
    - 然后用快捷键`C+a` + `D`迅速调出自己配置好的layout.
    - 迅速进入coding状态.
    - 在窗口见切换只需要`Alt + Arrow`
    - 一切操作都可以在各个panes中进行, 属实很方便呐!
   
##Debug
- 找不到`~/.tmux.conf`.(注意,这是个`文件`不是`文件夹`)
   - 安装完Tmux之后, 发现找不到`~/.tmux.conf`这个文件, 因此没办法进行更进一步的配置.
   - 搜索后才搞清楚, 如果没有这个文件, 就可以自己建一个. 于是用了下面的命令

             nano ~/.tmux.conf
   
   - 配置好后保存, 退出.然后问题又来了.
- 配置不生效.
   - 保存好配置文件后, 重新开启Terminal, 但是配置并没有生效. 
   - Google 关键词`~/.tmux.conf affect`
   - 找到了答案, 尽管关闭了Terminal, 但并没用重启Tmux server. 可以用这个命令`tmux kill-server` 杀死进程,然后使用如下命令

             tmux source ~/.tmux.conf    
             
   - Done!

- 反复试验Tmux很久之后发现自己开了很多session, 意识到原来关闭了Terminal之后并不会关闭Tmux-server.
    - 于是使用命令` tmux kill-server` 杀死server.
    - 但是问题来了, 每次重新开启之后并没有新建session.
    - Google 关键词`tmux session`后找到了答案.
       - 在`~/.tmux.conf`中添加一行代码
       
           > \#tmux attach 如果无分离终端则新建  
           > new-session
   - Done!

##感受
- 虽然Tmux给的快捷键很多, 一直间也记不过来, 但是只要把常用的几个熟练掌握, 把一些机械的流程配置好, 上手起来会非常快.
- 因为目前coding经验还不足, 随着未来做更多project, 相信对Tmux的配置也会帮助自己越来越高效!
- 写了几个教程之后发现, 其实写教程不仅仅是为了给别人看, 更是质问自己是否已经明白了教程中所有的点, 如果有没明白的地方, 就会发现那个地方怎么也写不清楚. 不写是真不知道自己写的有多差... 继续练习!  

##更新
151107 编辑  
151110 修改了参考文献.添加了官方文档, 并对参考文献做了适当说明.  
151112 修改了背景介绍.
##References
- [1][官方文档](http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man1/tmux.1?query=tmux&sec=1)
- [2]*<http://www.hamvocke.com/blog/a-guide-to-customizing-your-tmux-conf/>
  - 很多中文教程都是参考的这篇博文, 其中的解释非常清楚. 
- [3]*<http://www.cnblogs.com/congbo/archive/2012/08/30/2649420.html>
  - 这是一篇中文的指南, 其中对server, sesseion, window, pane解释的非常清楚. 
- <https://gist.github.com/barbour-em/e6fffc31482625cc4e0c>
  - 这篇一个非常完整的配置文件, 但是没有详细的解释, 对于配置有更高要求的同学可以看看.
- <http://lukaszwrobel.pl/blog/tmux-tutorial-split-terminal-windows-easily>
  - 很多教程也参考了这篇文章的内容. 
- <http://blog.chinaunix.net/uid-26285146-id-3252286.html>
- <http://os.51cto.com/art/201410/453671.htm>
- <http://blog.jobbole.com/87584/>
   - 这篇又有些新的东西值得日后挖掘. 
- <http://blog.csdn.net/jianbinhe1012/article/details/7741727>
- <http://media.pragprog.com/titles/bhtmux/code/config/tmux.conf>
- <http://unix.stackexchange.com/questions/66606/tmux-not-sourcing-my-tmux-conf>
   - 配置无法生效的时候参考了这篇的解决办法. 
