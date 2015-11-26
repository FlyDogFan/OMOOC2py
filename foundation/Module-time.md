# Module: time and datetime
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
 


##更新
151126 编辑


    