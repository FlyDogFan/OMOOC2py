#使用FLask框架
##背景
- 之前的每周的任务都是用的Bottle框架, 团队的三位小伙伴讨论后, 决定使用Flask框架.
- 原因:
   - 第三方库更多
   - 学习成本低, 因与Bottle很类似.
   - 这样就学会了两个框架;-) 



##学习过程
### 学习Flask框架基本用法
   - `request`与bottle中的`request`微微不同.
   - 形式为:
      - `request.form['XXX']`
      - `request.files['XXX']`

###如何存储图片信息
- Basic
    - 在html文件`form`中添加`enctype="multipart/form-data"`.只有使用了`multipart/form-data`，才能完整的传递文件数据，进行下面的操作.
    - 此处遇到了第一个bug, 就是如果图片的文件名为中文时, 存储的文件名就只截取后边的扩展名.
        - <http://tuzii.me/diary/52e9a4e49c20116d8ca80dd4/%E8%A7%A3%E5%86%B3fLask%E4%B8%ADsecure_filename%E8%8E%B7%E5%8F%96%E4%B8%AD%E6%96%87%E6%96%87%E4%BB%B6%E5%90%8D%E9%97%AE%E9%A2%98>
        - 比较笨的解决办法就是用`时间戳`作为文件名. 即将文件名命名为'[时间戳].[extension]`

- 限制上传图片大小 
    - `app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024`
        - 最大16 megabytes 

- 使用SAE Storage
    - 先看一段代码
    
    ```Python
    c = Connection()
    bucket = c.get_bucket('imges')
    bucket.put_object(filename, file.read()) 
    return bucket.generate_url(filename)
    
    ``` 
    - 1st line: 与storage建立连接.
    - 2nd line: 指针对应到文件夹`imges` 
    - 3rd line: 将文件名,文件存到`images`中.
    - 4th line: 返回这个文件名的链接.
    - 这样, 通过这样一段简单的代码就可以把图片保存到SAE storage中.
    - [代码](https://github.com/xpgeng/straypetshelper/commit/7a3552665b4f6e475e4c926e48351df4c71308da)        
  
###数据库设计.
- 现阶段使用KVDB

    > key = strftime("%y%m%d%H%M%S" , localtime())  
    > value = {'pet_title':pet_title, 'species': species,'location':location, 'tel':tel, 'supplement':supplement,'photo_url':photo_url,'time':time}  
    
    - 目前的设计比较简单, 随着功能的增加, 会逐渐修改
###基本功能
- 注册
    - 基于@huijuannan的模板, 修改成了注册的模板, 其中遇到的一个坑
       - `kv.set(key,value)`一直写不仅数据库, 因为是用`dev_server.py` 本地调试, 所以通过好几次print才确定是什么位置出现问题, 但是查不出原因.
       - 后来意识到可是key只能写str型, 于是用 type()检查了一下key的类型, 才发现我给的是'unicode', 于是用`str()`变形, Done!

- 登录
    - 原理跟注册类似, 只需要根据用户名, 找出数据库中的密码是否与输入密码一直即可.
     
###Templates

   
###备份


##Debug
- 图片为中文名称, 不包含任何jpg等等时,会出现错误.
- 图片名字如果重复, 则会覆盖之前的存储.
- 密码最少输入六位
- 用户名查重
- 检查email类型
- 页面跳转

##Refenrences
- [Flask官方文档](http://flask.pocoo.org/)
   - [Accessing Request Data](http://flask.pocoo.org/docs/0.10/quickstart/#accessing-request-data)
   - [File Uploads](http://flask.pocoo.org/docs/0.10/quickstart/#file-uploads)
- [SAE-storage](http://www.sinacloud.com/doc/sae/python/storage.html) 
   