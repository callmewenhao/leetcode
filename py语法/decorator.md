# decorator

> 建议看这个[知乎文章](https://zhuanlan.zhihu.com/p/160979609)
>
> decorator 就是对原有函数做了**修饰**，增加了新功能😁


下面这个例子很好地展示了 decorator @checker 的作用

其实就是，把被修饰的函数放入装饰器 checker() 函数中，然后使用其返回的 new_func() 函数处理参数

```python
def arg_check(x):
    return type(x) == int


def checker(func):
    def new_func(a, b):
        # 额外的功能
        if not arg_check(a) or not arg_check(b):
            return 0

        # 原来的功能
        return func(a, b)

    # 返回一个新的函数，这个函数增加了额外的功能
    # 并保留了原函数的功能
    return new_func


@checker
def add(a, b):
    return a + b


print(add(10, 100))
# 110
print(add(0., 100))
# 输入不是整数 
# 0 
```

















