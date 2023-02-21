# reduce() 函数

`reduce()` 函数会对参数序列中元素进行累积。 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：

用传给 `reduce` 中的函数 function（有两个参数）先对集合中的**第 1、2 个元素进行操作**，**得到的结果再与第三个数据**用 `function` 函数运算，最后得到一个结果。

```python
from functools import reduce
reduce(function, iterable[, initializer])

# function -- 函数，有两个参数
# iterable -- 可迭代对象
# initializer -- 可选，初始参数
# 使用示例
sum1 = reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
sum2 = reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数
reduce(gcd, nums)  # 计算数组中所有元素的最小公倍数
```

























