#Mydaily-Net

##Introduction
本版本基于之前local版的Mydaily, 发成现在的内网版的交互日记系统.目前还没有添加GUI界面.

##Function
- 客户端实时查看服务端保存的内容
- 支持多端查看与输入

##Installation
- 首先开启一个Terminal运行sever.py
- 再次开另一个Terminal运行client.py
- 输出`'pre'`查看过去信息.


##Troubleshooting
- 如果提示端口被占用, 更改sever和client脚本中的端口值(大于1024, 小于65535)
