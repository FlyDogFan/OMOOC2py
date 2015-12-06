#使用FLask框架
##背景
- 之前的每周的任务都是用的Bottle框架, 团队的三位小伙伴讨论后, 决定使用Flask框架.
- 原因:
   - 第三方库更多
   - 学习成本低, 因与Bottle很类似.
   - 这样就学会了两个框架;-) 



##学习过程
- 学习Flask框架基本用法
   - `request`与bottle中的`request`微微不同.
   - 形式为:
      - `request.form['XXX']`
      - `request.files['XXX']`

- 如何存储图片信息
    - 在html文件`form`中添加`enctype="multipart/form-data"`.只有使用了`multipart/form-data`，才能完整的传递文件数据，进行下面的操作.
  
- 数据库设计.





#Refenrences
- [Flask官方文档](http://flask.pocoo.org/)
   - [Accessing Request Data](http://flask.pocoo.org/docs/0.10/quickstart/#accessing-request-data)
   - [File Uploads](http://flask.pocoo.org/docs/0.10/quickstart/#file-uploads)
   