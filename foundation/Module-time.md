# Modules: time and datetime
##1. time stamp
- 在进行微信开发过程中, 发现微信传输的XML文件中, `creatTime`使用的是timestamp(时间戳).
- 查看当前时刻的时间戳.

    > import time   
    > time.time()
    
    - 输出以秒计算的float value, 例如: 1448531422.9
- 将时间戳转化为自定义格式时间.
   - 使用time.localtime(TimeStamp)
    
    > timeStamp = time.time()  
    > timeArray = time.localtime(timeStamp) 
   
   - 输出一个struct_time序列.
       
             time.struct_time(tm_year=2015, tm_mon=11, tm_mday=24, tm_hour=23, tm_min=7, tm_sec=46, tm_wday=1, tm_yday=328, tm_isdst=0) 
             
   - 转化成一个字符串格式的时间可以用 `time.strftime()`

    > Time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray) 
    
    - 输出类似于`2015-11-24 23:07:46`
    - 其中的格式可以随自己调整, 添加或省去任何时间信息. 详细的符号可以看[这里](https://docs.python.org/2/library/time.html?highlight=time#time.strftime)
    - 还有一点, 输出为struct_time的函数为
       - `time.localtime()`
       - `time.gmtime()`
- 还有一种直接的转化方式:`ctime(secs)`或者`acstime(localtime(secs))`

    > now = time.time()  
    > time.ctime(now)
    
    - 转化为固定格式:`Thu Nov 26 22:26:41 2015`


##2.timedelta
- `delta`在数学中通常指代变量的变化量.所以从这个模块的名字就可以看出, 这个模块可以用来指代时间的变化量.
- 下面介绍`timedelta`如何进行运算的.
    - print `timedelta(days=365)`, 可以看到
    
       > `365 days, 0:00:00`
       
       - 其中的`days`可以换成`weeks`, `hours`, `seconds`, `miliseconds`等等. 
       - 数字可以是`ints`, `longs`, `floats`, 可以是负数.
       - 每个不同的时间单位会有不同的变化区间.
    
    - 加法, 数乘
        - `10*timedelta(days=365)`
        - `timedelta(days=365)+timedelta(days=365)`
       
    - `timedelta(days=365).days`  
        - 将数字提取出来.
##3. date
- 只有年月日信息.
- 常用函数
   - `date(year, month, day)` 为date赋值. 
   - `date.today()` 查看今天日期.
   - `date.fromtimestamp(timestamp)`将时间戳转化成年月日
   - date的属性`.year`, `.month`, `.day`. 可以将一条date中的年月日提出来.
   - +/_`timedelta`
   - date之间进行加减数乘.
  




##注意
- 在边学边coding的过程中, 使用了`from datetime import *`, 终于出现这个弊端, 就是我同时使用 `import time`, 在运行`time.time()`发生了冲突. 原因是: datetime中也有time模块, 但是没有`.time()`这一属性.因此, 真的要尽量少用 `from XXX import *`.

##更新
151126 编辑  
151127 更新