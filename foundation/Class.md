#Class 学习笔记
##Why-为什么要学会用class.
- 之前所学的都是利用函数或各种语句来完成任务, 比如[Mydaily Version1.1](), 你可以看到就是根据所需要的功能一步一步的拼凑出来, 需要输入所以给个raw_input(), 需要写出到文件里, 所以就要用`.read()`,`.write()`等等.
- 那么可以看到, 完成以上任务, 我都是依据过程一步一步来做, 因此也叫作`面向过程`的编程.
- 那么我们换一个角度,  可不可以把我们要用的函数都封装在一起, 下次处理某些类似的事情的时候, 可不可以直接调用这个封装, 显然这样会更方便,尤其在处理大型程序的时候. 
- 这个时候就用到了class. `面向对象`的编程. 

##namespace
- namespace分为三部分
- 内建模块的namespace
- 自建的模块中的全局namespace
- 函数中的局部namespace

         Remark:不同namespace之间的name是没有任何关系的
         
- 表示一个object或者module的attribute:`modname.funcname`
- attribute是可读可写的.
    - `modname.the_answer = 42`;`del modname.the_answer`
- 不同的功能有不同的namespace, 比如读取模块的时候, 会创建全局namespace, 调用函数的时候, 又会有局部的namespace.

##Scope
- 搜索由里到外, 从最内部的scope开始-->调用函数的scope-->当前模块的scope-->内置模块的scope
- 理解
    - 函数有自己的域, 模块有自己的域, 内置模块的也有自己域.
    - 从最内层开始,一层层的搜索.
  
##定义
> class   ClassName:  
> ....def \_\_init__\(self):  
> ........print

##使用
> x = ClassName()  
> x.FunctionName()
- 这样即可调用class中的函数活着叫method.

##重要的method
- class中定义`def __init__(self,XXX):`
  - 可以把参数直接传到init中. 无需其他操作. 
- class中定义`def __del__(self,XXX):`
  - 当对象消逝不在被使用的时候,del就会启动.但是具体什么时候启动,如果希望有明确声明的花, 建议用 del函数.

##继承-Inheritance
- 理解:有基本类, 基本类中又想要用的函数, 然后在基本类的基础上构建子类, 子类有自己的特有的函数, 同时又要用到基本类中的函数.这就是继承.
- 多重继承: 子类调用多个基本类的函数.
- 格式:

    > class BaseClass:  
    > ....def __init__(self, XXX, YYY):  
    > class DerivedClass(BaseClass):  
    > ....def __init__(self, XXX, YYY, ZZZ ):  
      ........BaseClass.__init__(self, XXX, YYY)

##优点
- 代码更整洁, 方便移植和修改.
- debug非常方便.


##Q
- The defference between dynamic and static?





##更新
151030  沈浪编辑






