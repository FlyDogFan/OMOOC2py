Preparation
--
Before you create a gitbook, you should confirm that you have setup these tools in order.

- [Node.js](https://nodejs.org/en/)
- Gitbook-cli
   - for Mac users
         
            $ sudo npm install gitbook-cli -g
          
- Gitbook

            $ gitbook versions:install latest

- Git
- Calibre

>Some problems I face  in this part
>  
>  1. Can't use "npm install gitbook-cli -g" to setup gitbook-cli. 
> 
>    - 当时看到一堆error时，有点蒙，感觉无从下手，搜索也是本能的搜些诸如安装教程，gitbook 教程之类的关键词，看是否是我之前参考的教程有错还是咋的，然后又搜了“安装失败”,无果。 
>    - 仔细看了出错的语句，发现"Please try running this command again as root/Administrator."所以觉得可能时权限不足导致的，但是又不知道怎么能有权限（真的是终端指令白痴TT），于是终极搜索大法来了，直接把这句复制Google，搞定。
> 
> 2. Mistakenly regard gitbook-cli as gitbook
>    - 我以为gitbook－cli就是gitbook了，然后顺理成章的认为我已经安装好了，转而去折腾calibre（此处也有坑，稍后介绍），可是当我回过头来开始想要开始建立gitbook时，发现怎么也弄不了，仔细读了错误提示后才发现gitbook竟然没安上。  
>    - 搜索关键词  “gitbook 安装”，然后才发现要再来一行命令菜可以
> 
>              $ gitbook versions:install latest
> 3. ebook-convert cannot be added to global path
>  
>    - 使用命令
>         
>             $ ln -s /Applications/calibre.app/Contents/MacOS/ebook-convert /usr/bin   
> 
>    - 未遂。但是知道了 ln 是建立链接的意思，但还不清楚软连接与硬链接的区别
> 
>    - Google "ebook-convert  command  not found"  
>    - Replace /usr/bin with /usr/local/bin
>    - 目前仍然不明白原因。  
>   
>             收获： 直接Google，少走弯路。记住是 Google！
> 
> 

    
Guide
--


1. Create a new book repo [BookName] @[Gitbook](https://www.gitbook.com).
2. Create a new folder [BookName] @local.
3. Create README.md and SUMMARY.md 
 
        $ touch README.md and SUMMARY.md
        
4. Modify the book name @README.md.  
5. Edit SUMMARY.md
6. Initialize the folder with gitbook command.
   
        $ gitbook init
     
7. Initialize the folder with git 
        
        $  git  init
        
8. Add files

        $ git add README.md SUMMARY.md
         
9. Commit them

        $ git commit -m "write sth to explain this modification"
        
10. Add the remote gitbook repo in config.

        $ git remote add gitbook https://username:apitoken@git.gitbook.com/marshallshen/ruby-api-best-practices.git  
        
    - config locates in .git
    - You can use $ open .git  to find it
    -      
11. Pull the remote gitbook repo.

        $ git pull gitbook master 

12. Push files to remote gitbook repo.

        $ git push -u gitbook master
        
13. Creat a file book.json

        $ nano book.json
        
14. Add the plugin  Disqus in book.json

        {
         "plugins": [
            "disqus"
        ],  
        "pluginsConfig": {  
                  "disqus": {  
                  "shortName": "XXXXXXXX"  
             }
          }  
        }
        
      - register on [Disqus](disqus.com)
      - setting->add disqus to site
      - fill in Site URL，Site Name，Site Shortname
      - choose Advanced->Trust Domains->add
          
            gitbook.com
            gitbooks.io
(here  write the wrong shortname)
15. Push it to gitbook repo.
16. Creat a new github repo @github
17. Add the combination with github remote repo

        $ git remote add origin https://github.com/xpgeng/show-me-code.git
        
18. Push your files to github

        $ git push -u origin master
        
19. One command Double push

     - open .git and edit the config
     
              $ open .git
              
     - you will find like this

             [remote "gitbook"]
                 url = https://UserName:API-Token@git.gitbook.com/{{UserName}}/{{bookname}}.git
                 fetch = +refs/heads/*:refs/remotes/origin/*
            [remote "origin"]
                 url = https://github.com/{{UserName}}/{{RepoName}}.git 
                 fetch = +refs/heads/*:refs/remotes/origin/*   
                 
     - Merge them  

            remote "origin"]
                 url = https://github.com/{{UserName}}/{{RepoName}}.git 
                 url = https://UserName:API-Token@git.gitbook.com/{{UserName}}/{{bookname}}.git
                 fetch = +refs/heads/*:refs/remotes/origin/*   
        
     - Then everytime you push, you just only type

             $ git push -u origin master
             
     - This is called  "DOUBLE PUSH"   ;-)

20. Enjoy your Books! 
 

The problems I faced
--
1. 省略了step.11，直接来到step.12，结果有如下提示：
           
         error: failed to push some refs to 'https://xpgeng:kimshe523@git.gitbook.com/xpgeng／
         omooc2py.git'hint: Updates were rejected because the tip of your current branch is behindhint: 
         its remote counterpart. Integrate the remote 
         changes (e.g.hint: 'git pull ...') before pushing again.
         
   - Reason: 没有把remote repo pull到local 进行合并。
   - 于是，pu之！ done！
2. Merge过程中，我local已经有了chapter1.md，注意c是小写，可是合并时候gitbook自动给出了Chapter1.md，并且提示无法合并。反复修改删除无果。
    - 怒删这俩文件。从新建立。
    - 我感觉的原因
          - 章节的题目建的是 Chapter 1.所以系统生成了Chapter1.md  所以合并的时候由于两个都链接到章节题目，由于命名不同所以导致没法合并。
          - 还没有进一步验证。

3.  Cannot link gitbook to github 
     
    - 点了Add webhook，但是没有任何反应，Github中也没有任何链接的提示。
    - Google 关键字 gitbook link to github. 无果。
    - 后来找了Samy Pesse的github主页，在上边留言说明了自己的问题。他很快就回复了我，在gitbook 的add webhook 下边加了一个手动添加到github webhook的连接。
    - 手动添加后，done！Thanks Samy！
  

References
==

- <https://openmindclub.gitbooks.io/omooc-py/content/support/gitbook.html>
- <https://jeremiahzhang.gitbooks.io/gitbookguide/content/plugin/disqus.html>
- <http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013752340242354807e192f02a44359908df8a5643103a000>
- <https://help.gitbook.com/github/transferring_to_github.html>
- <http://blog.sina.com.cn/s/blog_605f5b4f010194fg.html>


Thanks
==
[Samy Pessé](https://github.com/SamyPesse)  
[Lei Yu](https://www.gitbook.com/book/jeremiahzhang/gitbookguide/details)  
[OpenmindClub](https://github.com/OpenMindClub/OMOOC2py)











         