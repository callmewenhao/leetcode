# yield

> Generator objects 无栈协程/轻量级线程 [官方文档](https://docs.python.org/zh-cn/3/reference/expressions.html#yield-expressions)
> 
> 个人总结：
> yield 相当于 **保留函数现场** 的 return，返回的生成器对象一般使用 next() 得到真正的返回值。
> 生成器对象首次执行从函数的第一条语句执行，但是之后的每次执行都是从 yield 后面的语句开始执行，
> 包括把 yield 表达式的值付赋给其他变量。

yield 表达式在定义 generator 函数或 asynchronous generator 函数时才会用到因此只能在函数定义的内部使用。

在一个函数体内使用 yield 表达式会使这个函数变成一个**生成器函数**，
而在一个 async def 函数的内部使用它则会让这个协程函数变成一个**异步生成器函数**。 例如:

```python
def gen():  # defines a generator function
    yield 123

async def agen(): # defines an asynchronous generator function
    yield 123
```

生成器函数与协程非常相似；它们 yield 多次，它们具有多个入口点，并且它们的执行可以被挂起。
唯一的区别是生成器函数不能控制在它在 yield 后交给哪里继续执行；控制权总是转移到生成器的调用者。

## 生成器-迭代器的方法

> 下面的函数用于控制生成器函数的执行

1. generator.\__next\__() 略

2. generator.send(value)

    恢复执行并向生成器函数“发送”一个值。 `value` 参数将成为当前 `yield` 表达式的结果。 
`send()` 方法会返回生成器所产生的下一个值， 或者如果生成器没有产生下一个值就退出则会引发 `StopIteration`。 
当调用 `send()` 来启动生成器时， 它必须以 `None` 作为调用参数，因为这时没有可以接收值的 `yield` 表达式。

举例
```python
>>> def numbers():
...     i = 0
...     while True:
...         ret = yield f"{i:b}"
...         i += ret
...
>>>
>>> n = numbers()  # 函数返回一个生成器对象 n
>>> type(n)  # 查看 n 的类型
<class 'generator'>
>>> n.send(None)  # 使用 send 启动生成器
'0'
>>> n.send(1)  # 传入参数 1 输出 0 + 1 的二进制
'1'
>>> n.send(1)  # 传入参数 1 输出 1 + 1 的二进制
'10'
>>> n.send(1)  # 传入参数 1 输出 2 + 1 的二进制
'11'
>>> n.send(1)  # 传入参数 1 输出 3 + 1 的二进制
'100'
>>> n.send(2)  # 传入参数 2 输出 4 + 2 的二进制
'110'
>>> n.send(4)  # 传入参数 4 输出 6 + 4 的二进制
'1010'
```

```python
>>> def f():
...     a, b = 1, 2
...     while True:
...         yield b
...         a, b = b, a + b
...
>>> fi = f()
>>> next(fi)
2
>>> next(fi)
3
>>> next(fi)
5
>>> next(fi)
8
>>> next(fi)
13
```






