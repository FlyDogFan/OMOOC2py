如何实现push160
--
#Remark
目前只做了输出一个git config文件, 离真正一键push160还有段距离,敬请期待....;-)
#Code of  Push160
```
import csv                            
from sys import argv
from os.path import exists             

script, csv_file, copy_file = argv

exists(copy_file)

config = open(copy_file,'w')


#此部分为config链接前面的所有字符
head = """                           
[core]
\trepositoryformatversion = 0
\tfilemode = true
\tbare = false
\tlogallrefupdates = true
\tignorecase = true
\tprecomposeunicode = true
[remote \"OMOOC2py\"]
"""
config.write(head)


#此部分为链接部分
with open(csv_file, 'rU') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        config.write("\turl = %s/OMOOC2py.git\n" %row['username'])


#此部分为剩下所有字符
end = "\tfetch = +refs/heads/*:refs/remotes/OMOOC2py/*"
config.write(end)

print "done"

#copy_file.close()        

```

[Push60_beta Download](https://github.com/xpgeng/Road-to-Py)  

- 使用方法:$ python [csvfile_name] config  
- config 其实可以改写成任意一个你改写的文件名, 通过修改这个shell, 你可以做到将csv文件的内容写入到任意文件. 
#目标
- 用Python脚本，根据160位同学的github账号、gitbook账号列表, 读取该列表，然后拼出git config文件内容.
- 该列表通常为csv列表.
- 经过配置之后实现一条口令push160. 


#背景
- 感谢@小赖 同学的双推shell, 同样也是在@一休的启发下, 才有了如何一条口令push到160个repo的任务, 并且@一休也给出了任务分解的思路, 甚至连如何完成的帮助文档链接都给了出来.
- 为什么要push160?
   - 阳老的一句话非常打动我, 大意就是你自己可能花费了一点时间去做这个东西, 可是这也就意味着有160个人不用在花费同样的时间去完成它, 转而可以将时间花在更重要的事情上.这意味着你节省了160倍的时间.
   - 再次建议大家读一读[如何成为一名黑客](http://translations.readthedocs.org/en/latest/hacker_howto.html)
- 什么是csv文件
   -  Comma-Separated Values (CSV) files
   -  文件的每一行都是一个data record
   -  每个data record 又被 ","或者":" 亦或";"分隔成几部分.
   -  以上就是csv文件的基本格式,举个栗子.
   
   > Year,Make,Model,Description,Price   
1997, Ford, E350, "ac, abs, moon", 3000.00    
1999,Chevy,"Venture ""Extended Edition""","",4900.00   
1999,Chevy,"Venture ""Extended Edition, Very Large""",,5000.00     
1996,Jeep,Grand Cherokee,"MUST SELL!air, moon roof, loaded",4799.00

   - 再来个栗子  
   
   > Year;Make;Model;Length   
     1997;Ford;E350;2,34    
     2000;Mercury;Cougar;2,38
#任务分解

- 读取csv文件
- 输出csv文件写入到config文件
- 拼接语句使其符合config文件格式


Ps: 当你看完代码的时候,你会发现这就是 learn Python the hard way前21课的内容回顾.


#详解



- 读取csv文件
   - 先上马
     
    ```  
    import csv
    with open('name.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
        print row
    ```
  - 这是copy了Python官方文档里给的标准例子,我用这个代码套到一休给的csv文件时,我遇到了一个一点都不严重的问题,***读不出来*** .....哭晕在厕所 
  
    >_csv.Error: new-line character seen in unquoted field - do you need to open the file in universal-newline mode?   

  - 标准套路就是先看官方文档嘛, 这个我懂..看上文的意思就是要不要在某个模式下打开文件,于是乎,先查查open函数再说,恰好看到有 universal newline的字样, 先不管什么意思,试试再说, 将 open()中的 'rb' 改为'rU'.   ***读. 出. 来. 了.!***
  - 时间有限,我还没来得及去仔细阅读其中的缘由.
  - 其实本来是想起不知道哪位开智群友说的, 要时刻围绕着问题, 别跑偏, 于是我还是继续好了.这里也提醒大家, 有问题解决了之后, 要赶紧进行下一步, 等到达到最终目的后, 在回过头来去查缺补漏, 否则一头扎进文档里, 半夜三点,发现才刚读出文档,岂不是很悲催. 


- 如何读取csv文档写入到config文件

   - 这里我上来就***蒙了***,看前面的代码, 你可以看到, 它是一个for循环, 每次都是输出一行,然后循环输入, 可是在写入到config文件里时,怎么才能让他循环的写,而又不会被覆盖?
   - 胡乱尝试各种写法, 打开config文件里面都是空的. 没办法, 关键词搜索"Python" "for循环" "write"
   - 终于发现还可以这么写

    ```
    for row in reader:
        config.write("url = %s /OMOOC2py.git\n" %row['username'])
        
   - 原谅我的无知..我是真不知道write里面花样可以这么多..

- 如何让出输出到config文件的内容符合config文件格式
   - 这个就属于拼接文字了, 我用的比较笨的办法
   
   ```
   head = """
		[core]
		\trepositoryformatversion = 0
		\tfilemode = true
		\tbare = false
		\tlogallrefupdates = true
		\tignorecase = true
		\tprecomposeunicode = true
		[remote \"OMOOC2py\"]
		"""
config.write(head)
   ```
   - 以及
   
   ```
   end = "\tfetch = +refs/heads/*:refs/remotes/OMOOC2py/*"
	config.write(end)
	```
	- 这样就把头尾都写到config里, 中间夹上csv文件的数据即可.

#体会	
- 以上就是输出整个config文件的基本思路, 其实当把任务分解开后, 你会发现没什么技术含量, 只需要对要用到的函数熟悉即可.所以, 我也是花了很多时间在了解函数如何用上.
- 因为以前真的是没有编过什么东西,所以即使@一休把任务已经分解好, 上手的时候还是挺蒙的, 看啥都新鲜, 一脸的迷茫
- 所以我在领到任务后发现很多基本函数自己不了解后,果断转到看笨办法,尤其是15课开始, 当我在看的时候总会联想到自己要做的任务, 书中给出一个例子, 自己马上就能围绕任务做一个简答小例子尝试一下, 反而学的更深刻.
- 大家都在讨论什么时候用"笨功夫", 我觉得在学习基础的时候, 就得用笨功夫, 比如喜欢跑步, 笨功夫花在什么上? 可以考虑花大量时间在技术动作上, 没有个好的,合理的,有效率的,正确的技术动作, 即使跑的再长也没有用, 受伤只是时间长短的事, 受伤意味什么? 呵呵,前边半年白跑了...T_T, 请不要学我..
- 但是这里又要注意,"笨功夫"可不是脑子什么都不想, 就低头苦干, 要注意***反馈***
- 没有***反馈***的练习都是耍流氓!
- 练习前边其实还有两个字, 刻意. 


#所用函数
1. import  XXX
2. open()
3. exists()
4. with..as..
5. .DictReader()
6. .write()
7. for .. in ..:


Ps: 你会发现基本上都是"笨办法", 就像大妈说的, 真的是只学会前21课就可以做了.


#未解决的问题
1. 代码后边 #copy_file.close(), 为什么加上之后就提示用不了. 
2. 目前只是有config文件, 但是还没发推送到每个人的库, 之前跟@wp-xiaolai尝试互相推到对方的库, 需要ssh, 而且仅限一个库. 推多库的办法官方文档中又介绍, 下一步会研究一下,有兴趣的同学欢迎一起讨论.
3. 还没弄清楚config文件中[core]中的那几行都是什么含义.


#References
<https://en.wikipedia.org/wiki/Comma-separated_values>
<https://docs.python.org/2/library/csv.html?highlight=csv#csv.writer>
<https://www.python.org/dev/peps/pep-0305/>
<http://stackoverflow.com/questions/17315635/csv-new-line-character-seen-in-unquoted-field-error>












