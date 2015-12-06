#多人开发Git-CLi
##背景


##基本CLI

- 创建`dev`分支，然后切换到`dev`分支:

    > $ git checkout -b dev
    
    相当于
    
    > $ git branch dev  
    > $ git checkout dev

- 查看当前分支

    > $ git branch
    
- 切换回master分支

    > $ git checkout master
    
- 把`dev`分支的工作成果合并到`master`分支上

    > $ git merge dev
    
    - 这种合并, 如果删除了分支, 就会丢掉分支信息, 即,不会从分支历史中看到曾经合并过的分支信息, 推荐用下面的命令.
    
    > git merge --no-ff -m "XXXXX" dev
    
    - 其中`ff`的意思为: fast forword 模式. 
    - 在这种模式下，删除分支后，会丢掉分支信息, 所以用上边的命令禁用`ff模式`.
    
- 删除`dev`分支

    > $ git branch -d dev
    
    - `-D`为强行删除.
    
- 查看分支合并图

    > $ git log --graph
    
    - 此处有待深挖

- 为版本打标签

    > $ git tag v1.0   <commit id>
    
    - 省去`<commit id>` 则给最新一次的commit id 打标签.

    > $ git tag -a v0.1 -m "version 0.1 released" <commit id>
