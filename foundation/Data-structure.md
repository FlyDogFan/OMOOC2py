#Data Structures

##1. list
- 首先要清楚list长什么样

    > list = [ ]
    
- Using list as stacks
   - 后进先出. 
   - `.append()`, `.pop()`
- Using Lists as Queues
   - 先进先出 
   - `.append()`, `.popleft()`
- three built-in functions
   - `filter(function, sequence)` 
      - 将序列逐一带入到函数中, 返回True的元素组成一个list输出.
   - `map(function, sequence)`        
      - 这个函数意思就是给定一个序列如`range(X,XX)`, 不断将序列带入到函数中, 并返回输出一个list.
      - 如果函数需要两个参数, 可以再添加一个序列,依次类推.
- 利用列表推导式快速创建列表.
   - 例: `squares = [x**2 for x in range(10)]`
   - `[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]`
   - `[abs(x) for x in vec]` , 可以应用各种函数.
   - `[weapon.strip() for weapon in freshfruit]` , 应用method.
   - `[(x, x**2) for x in range(6)] `, 逐一, 一定要用括号`()`. 
   - `[num for elem in vec for num in elem]`, for循环中有for循环,
   - `[[row[i] for row in matrix] for i in range(4)]`, 嵌套的list, 这样可以处理一个矩阵, 输出也为一个矩阵. 
      - `zip(x,y,z,...)`: 返回一个列表, 列表里每个元素是个数组, 第一数组就是x,y,z...中的第一个元素, 依次类推. 功能上跟上边类似, 但是这是一个build-in function.

## 2. del
- 就是删除啊!!
- del a[2]
- del a[1:5]
- del a 

##3. Tuples
- tuple的定义: A tuple consists of a number of values separated by commas
- 特点:
   - 可以嵌套
   - 无法像列表一样元素被改变. 但是数组里的元素可以使一个list.
- 如何构造?
   - `singleton = 'hello',`
   - `singleton = () `

 