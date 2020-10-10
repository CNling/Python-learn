# Python基础-2

## 流程控制语句

### 条件判断语句

- if

	- 语法：
	- 代码块：一组代码

- if-else

	- 语法：

- if-elif-else

	- 语法：

### 循环

- while

	- 语法：同if
	- 三要件（表达式）

		- 初始化表达式，初始化变量
		- 条件表达式：循环执行的条件
		- 更新表达式：更新初始变量的值

- for

	- 语法：

- 循环终止

	- break：跳过整个循环包括 else
	- continue：跳过指定的一次或多次循环
	- pass： 占位

### 缩进

- tab
- spaces（4个）

### input()

- 获取用户输入
- 参数：字符串
- 返回值：字符串
- 阻止程序结束

## 序列（squence）

### 数据结构

- 计算机中存储数据的方式

### 有序的数据

- 每一个数据都有唯一的索引，按添加的方式分配索引

### 分类

- 可变序列

	- 字典

		- 数据结构

			- 映射（mapping）

		- 存储对象的容器

			- 每个对象拥有唯一的名字（键）

		- 存储性能很差，查询性能很好
		- 语法：{键：值，键：值}
		- 值（value）

			- 任意对象

		- 键（key）

			- 任意不可变对象

		- 创建

			- 使用{}

				- {k1:v1,k2:v2,k3:v3}

			- 使用dict()函数

				- d.dict(name = 'sunwukong', age = 18)
				- 将包含双值子序列的序列转换成字典

					- [('name','sunwukong',('age',18)]

		- 操作

			- len()

				- 获取字典中键值对的个数

					- len(d)

			- in

				- 检查键是否存在于字典中

			- not in

				- 检查键是否不存在于字典中

			- d[key]

				- 根据键获取字典中的值

			- get(key[, default])

				- 根据键获取值，若不存在，返回None或返回指定的默认值

					- d.get('name','该值不存在')

		- 修改

			- d[key] = value

				- key存在则覆盖，不存在则添加

					- d['name'] = 'qitian'

			- update([other])

				- 将其他字典中的key-value追加到当前字典中

					- d1.update(d2)

			- setdefault(key[, default])

				- key存在则返回key的值，不存在则将key添加至字典，并设置value

					- result = d.setdefault('name', '猪八戒')

		- 删除

			- del

				- del d['name']

			- pop(key[, default])

				- d.pop('name','默认值')

					- result = value

			- popitem()

				- 随机删除一个键值对，一般删除最后一项

					- result = (key,value)

			- clear()

				- 清空字典

		- 复制

			- copy()

				- 浅复制,当值是一个可变对象时，这个可变对象不会被复制

					- d2 = d1.copy()

		- 遍历

			- keys()

				- 返回一个序列，序列中包含所有的键

					- for k in d.keys():

			- values()

				- 返回一个序列，序列中包含所有的值

					- for v in d.values():

			- items()

				- 返回一个序列，序列中包含双值子序列（key，value）

					- for k,v in d.items():

	- 列表（list）

		- 可变对象

			- 可以存储对象
			- 修改对象

				- 通过变量修改对象的值

					- my_list[0] = 10

				- 不会改变变量所指向的对象
				- 当修改的对象被多个变量所指向时，所有的变量都会发生变化

			- 修改变量

				- 为变量重新赋值

					- my_list = [q,w,e,r]

				- 改变变量所指向的对象
				- 重新赋值不会影响其他变量

			- 一般为变量重新赋值是修改变量，其余的是修改对象

		- 创建

			- my_list = [ ]

		- 操作

			- 添加：my_list = [1, "hello", True, input]
			- 提取元素：my_list[索引]   my_list[ 0 ]
			- 获取长度：len(my_list)
			- 切片：my_list[起始：结束：步长]

				- my_list[0:5:2]
				- 包含起始元素，不包含结束元素，[ )区间
				- 步长默认为1，不能为0，可以是负数

			- +，*

				- [ ]+[ ]：将两个列表拼接成一个列表
				- [ ]*3：将列表中的元素复制3份

			- min（），max（）

				- min(my_list)：获取列表中的最小值
				- max(my_list)：获取列表中的最大值

			- in，not in

				- 1 in my_list：检查元素是否存在于列表中
				- hello not in my_list：检查元素是否不在列表中

			- index()

				- my_list.index(1,0,5)

					- 获取元素1在列表中第一次出现时的索引，从索引0开始查找，到5结束，不包含5

				- 方法（method）

					- 与对象关系紧密的函数
					- 通过 对象.方法() 调用

			- count()

				- my_list.count(1)

					- 统计元素1在列表中出现的次数

		- 修改

			- 通过索引修改

				- my_list[0] = 'hhh'

					- 将序列为1的元素替换为‘hhh’

				- del my_list[0]

					- 删除序列为1的元素

			- 通过切片修改

				- my_list[0:2] = ['swk','zbj']

					- 使用新的替换旧的元素

				- my_list[0:0] = ['blm']

					- 在索引为0的前面插入元素

				- my_list[::2] = ['J','Q','K']

					- 使用步长后，序列中的元素的个数必须和切片中元素的个数一致

				- del my_list[0::2]

					- 删除步长为2的元素

				- my_list[0:3] = [ ]

					- 删除索引为0-2的元素

			- 不可变序列修改

				- s = list(s)

					- 使用list()函数

		- 方法

			- 添加

				- my_list.append('美猴王')

					- 在列表的最后添加一个元素

				- my_list.insert(2,'美猴王')

					- 指定位置插入，指定元素

				- my_list.extend(['孙悟空','美猴王'])

					- 将参数中的序列添加至当前列表中

			- 删除

				- my_list.clear()

					- 清空

				- result = my_list.pop(2)

					- 根据索引删除，并返回被删除的元素，若没有参数则删除最后一个元素

				- my_list.remove('美猴王')

					- 删除指定值的元素，若有多个则删除第一个

			- 反转

				- my_list.reverse()

					- 反转列表

			- 排序

				- my_list.sort(reverse=False)

					- 对列表中的元素进行排序，默认是升序，将False改为True变为降序

		- 遍历

			- while 循环
			- for 循环

				- range()

					- 生成一个自然数的序列
					- (起始，结束，步长)
					- for i in range(10):

- 不可变序列

	- 字符串（str）
	- 元组（tuple）

		- 创建

			- my_tuple = ()
			- my_tuple = 1,2,3,4
			- my_tuple = 1,

		- 操作

			- 与列表（list）的操作一致

		- 解包（解构）

			- my_tuple = 1,2,3,4

				- a,b,c,d = my_tuple

			- a = 1, b= 2

				- b, a = a, b

			- a, b = my_tuple

				- 解包时，变量的数量必须和元祖中的元素的数量一致

			- a, b, *c = my_tuple

				- 变量前加 * 可以获取所有剩余的元素，并以列表保存

### 集合(set)

- 与列表非常相似
- 不同：

	- 只能存储不可变对象
	- 存储的对象无序：并不是按照元素的插入顺序保存
	- 不能出现重复的元素

- 创建

	- s = {1,2,3}
	- s = set()

		- set()函数可以将列表和字典转换为集合，字典只会包含键

- 操作

	- len(s)
	- s2 = s.copy()

- 添加

	- s.add('hello)
	- s.upadte(s2/[ list ]/[ dict ]}

- 删除

	- s.pop()

		- 随机删除集合中的一个元素

	- s.remove('hello')
	- s.clear()

- 运算

	- &

		- 交集

	- |

		- 并集

	- -

		- 差集

	- ^

		- 异或集

	- <=

		- 判断a集合是否是b集合的子集

			- 若是，b为a的超集

	- <

		- 判断a集合是否是b集合的真子集

			- 若是，b为a的真超集

	- >

		- 同上

	- > =

		- 同上

*XMind: ZEN - Trial Version*