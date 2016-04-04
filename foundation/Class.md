#Class 学习笔记
##Why-为什么要学会用class.
- 之前所学的都是利用函数或各种语句来完成任务, 比如[Mydaily Version1.1](), 你可以看到就是根据所需要的功能一步一步的拼凑出来, 需要输入所以给个raw_input(), 需要写出到文件里, 所以就要用`.read()`,`.write()`等等.
- 那么可以看到, 完成以上任务, 我都是依据过程一步一步来做, 因此也叫作`面向过程`的编程.
- 那么我们换一个角度,  可不可以把我们要用的函数都封装在一起, 下次处理某些类似的事情的时候, 可不可以直接调用这个封装, 显然这样会更方便,尤其在处理大型程序的时候. 
- 这个时候就用到了class. `面向对象`的编程. 


##核心概念
- class
- method
- object
- instance
- attribute
- constructor
- inheritance



##Example
```python
class Book:     #this is class
    x = 0       #attribute
    name = ""
    
    def __init__(self,name): # common used  method and constructor
        self.name = name

    def readtimes(self):    # method
        self.x = self.x + 1
        print "%s was read %s times." %(self.name, self.x)
    
    #def __del__(self): # seldom used method and destructor
    #    print "I'm deleted...", self.x


class PyBook(Book): #inheritance
    times = 0
    
    def borrowtimes(self, borrower):
        self.readtimes()
        self.times = self.times + 1

        print "%s was borrowed %s times by %s." %(self.name, self.times, borrower)



a = Book("complexity")
a.name
a.readtimes()

b = PyBook("Core of Python")
b.name
b.borrowtimes("Sally")
b.borrowtimes("Sabie")
```




##method
- class中定义`def __init__(self,XXX):`
  - 可以把参数直接传到init中. 无需其他操作.
  - 这个比较常用, 从例子中也可以看到他传递参数的过程.直接通过class传递.
  - 对于method的参数传递可以看到一点区别. 
- class中定义`def __del__(self,XXX):`
  - 当不再使用某个object时,用`del`函数.
  - 不常用.

##继承-Inheritance
- 理解:已知一个基本类, 又构建了一个类, 这个类需要用基本类中的methods, 于是我们通过下面的语法就可以在新构建的类(子类)中调用基本类(父类)中的所有methods.这就是继承.
- 多重继承: 子类调用多个基本类的函数.
- 格式:

    > class BaseClass:  
    > ....def __init__(self, XXX, YYY): 
    >
    > 
    > class DerivedClass(BaseClass):  
    > ....def __init__(self, XXX, YYY, ZZZ ):  
      ........BaseClass.__init__(self, XXX, YYY)


##怎么用Class
- 新建一个object, 如果我们对于这个object初始就有一些属性要求, 比如初值, 或者一些method的要求, 那么我们就可以使用一个Class, 通过这个class来建立objects.



##优点
- 代码更整洁, 方便移植和修改.
- debug非常方便.
- 容易复用.


##Q
- The defference between dynamic and static?





##更新
151030  沈浪编辑






