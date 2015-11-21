#A Guide of Oh-my-zsh

    工欲善其事，必先利其器!

##Background
大妈在视频演示展示了酷炫的Bash-it, 其中提到了非常好用的oh-my-Zsh, 其功能与Bash-it相似, 非常强大且都是开源软件.于是, 本着好奇害死猫的精神, 探索一下Oh-my-Zsh.  
照例:

     系统: OS X 10.11

##Introduction
- Zsh: Z shell
   - 在了解Zsh之前, 先要了解一下什么是`Shell`
      - 看字面意思, 知道他是个`壳`. 是的, 他是Linux\Unix的外壳, 或者说媒介. 我们将命令(CLI-Command Line)输入到这个壳中, 他会将命令转化成系统能理解的语言, 这样我们就可以命令系统去执行一些我们想做的事情.
      - 我们有很多衣服, 同样的, 我们也拥有很多`Shell`.
      
                $  cat /etc/shells 
      - 输入上边的命令我们可以看到:
      
      ![shells](http://7xnwxz.com1.z0.glb.clouddn.com/%20cat%20%3Aetc%3Ashells.png)
      
      - 目前OSX系统默认的都是`bash`这个shell.但是我们现在介绍的这个shell`zsh`, 哼哼, 用了都说好!
   - 更多的了解可以参考这篇[Zsh简介](https://www-s.acm.illinois.edu/workshops/zsh/toc.html)
      - 这篇出自[Larry P.Schrof](http://www.schrof.net/)之手, 看了下他的自我介绍, 还挺cool的. 写的了程序, 玩得了音乐, 现在就职于Facebook.
   - 很多人一看到配置Zsh那么复杂繁琐, 基本上`4.2分钟`后, 纷纷关掉页面接着用`Bash`了. 这时候,`Oh-my-zsh`出厂!
- Oh-my-zsh
     - 让你一边配置`zsh`, 一边喊`Oh!my!Zsh!`.
     - 是的, 他就是一个管理zsh各种配置的工具, 其中包含了各种函数, 插件, 主题, 而且完全可以各种私人定制.因为他是开源的!
     

##Installation
###zsh
- 首先要检查是否已经安装Zsh.
           
        $ zsh --version
        
- 通常OSX已经安装好zsh, 但如果没有, 请输入以下命令:

        $ sudo apt-get install zsh
        
- 把zsh设置为默认Shell
        
        $ chsh -s $(which zsh)
        
- 退出再进入Terminal, 检查一下是否已经更改成功
       
        $  echo $SHELL
        
- 以上的任何步骤如果出现错误, 42秒内无法解决的话, 请及时Google it.

###oh-my-zsh
- 我们可以通过一下CLI安装
   
        sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
        
        或者
        
        sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
        
        
    
    ![done](http://7xnwxz.com1.z0.glb.clouddn.com/intall%20oh%20my%20zsh.png)

##Configuration

### Add plugins 
- 首先看一下[插件列表](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins).
- 添加插件只需要我们编辑文件`~/.zshrc`

        open ~/.zshrc
        
     ![open ~/.zshrc](http://7xnwxz.com1.z0.glb.clouddn.com/~%3A.zshrc.png)
        
- 找到类似下面这行代码, 在里面添加我们需要的插件名称即可.例如:


        plugins=(git textmate ruby osx ) 
        
- 每个插件的功能可以到对应的README中找到详细的解释.例如git 提供了以下alias:

|Alias	|Command|
|------|:-----:|
|g     |git  |
|ga	   |git add|
|gaa	|git add --all|
|gc	   |git commit -v
|gp	    |git push|

###Add aliases
- 由于有些CLI是自己经常使用的, 所以可以添加Alias使得常用CLI变成简单的几个字符, 大大节省时间.
- 添加方法类似添加插件, 同样是编辑文件`~/.zshrc`, 将类似如下格式的代码添加到文件中. 例如:

          alias cls='clear'
          alias ll='ls -l'
          alias la='ls -a'

- So easy!
- Remark:在这里我遇到了一个坑, 在添加别名的时候`' '`会变成中文标点符号.目前的解决办法就是把别的行的`' '`复制过来.我觉得是输入法的问题. 但是各种调试还未解决.这里算留个坑. 日后给出详细的分析, 解决办法.

###Change themes
- `Oh-my-zsh`还提供各种主题, 在文件`~/.zshrc`中可以看到如下代码:
    
          ZSH_THEME=”robbyrussell”
          
- 更改主题只需要更改名称即可.主题列表可以在`~/.oh-my-zsh/themes`中找到, [这里](https://github.com/robbyrussell/oh-my-zsh/wiki/themes)每个主题的图片.

##My Configuration
因为我也是刚刚开始折腾, 目前的配置还很初级, 随着各种类型的编程需求, 也会逐渐丰富配置, 越用越顺手.
###Plugins
目前我只添加的以下几个插件:
- git 
- brew
- github

###Theme
- 由于主题众多, 并不一定每个主题完全让自己满意, 所以, 我自制了一个主题.
- 方法如下:
     - 挑选功能. 去主题列表里找到自己需要的功能.
     - 在Terminal中输入`open ~/.oh-my-zsh`
     - 在Themes文件夹中新建一个`theme_name.zsh-theme`, 然后把需要的功能复制到里面, 保存好.
         - 近期会补充一下每行代码的作用是什么. 
     - 更改主题, 重新打开一个Terminal, 检查是否如自己要求.
     - OK!
     - 以下是我的主题代码以及效果图.
     
     ```
     local ret_status="%(?:%{$fg_bold[green]%}➜ :%{$fg_bold[red]%}➜ %s)"
PROMPT='${ret_status}%{$fg_bold[green]%}%p %{$fg[cyan]%}%d %{$fg_bold[blue]%}$(git_prompt_info)%{$fg_bold[blue]%} % %{$reset_color%}➜ '
ZSH_THEME_GIT_PROMPT_PREFIX="git:(%{$fg[red]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg[blue]%}) %{$fg[yellow]%}✗%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_CLEAN="%{$fg[blue]%})"

     ```
     ![my theme](http://7xnwxz.com1.z0.glb.clouddn.com/my-theme.png)

##Debug
- 将本文章push到gitbook一直不成功, 找了半宿加一上午的毛病,才发现文件的首字母大写了, 写到SUMAARY.MD里的是小写的. 虽然本地能够在SUMMARY.MD文件中点击打开打开, 但是push到gitbook后,却识别不了文件! 我这版本退回, 删除, pull, push,一通大招下去, 结果..是这么回事...好了.. 我去吐血了.

##更新
151104  编辑  
151105  修改   


##References
- <http://zhuanlan.zhihu.com/mactalk/19556676>
- [oh-my-zsh](http://ohmyz.sh/)
- <https://github.com/robbyrussell/oh-my-zsh/wiki/Plugin:git>
- [Github of oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)
- <http://blog.chinaunix.net/uid-26495963-id-3193686.html>


