# 二分查找

## Python API: bisect 模块
参数：a:待查找的对象，num：待查找的数字

| Syntax               | Description                         |
|----------------------|-------------------------------------|
| bisect_left(a, num)  | 查找目标元素左侧插入点,<br/>等价于C++中的 lower_bound() |
| bisect_right(a, num) | 查找目标元素右侧插入点,<br/>等价于C++中的 upper_bound() |
| bisect(a, num)       | 同 bisect_right()                    |
| insort_left(a, num)  | 查找目标元素左侧插入点，并保序地插入元素                |
| insort_right(a, num) |   查找目标元素右侧插入点，并保序地插入元素|
| insort(a, num)       | 同 insort_right()|

示例
```python
from bisect import insort_left
insort_left(self.buf, num)

# bisect_left 注意 返回的是下标
bisect_left(a, x, lo=0, hi=len(a), *, key=None)
# The returned insertion point i partitions the array a into two halves 
# so that all(val < x for val in a[lo : i]) for the left side 
# and all(val >= x for val in a[i : hi]) for the right side.
# key specifies a key function of one argument 
# that is used to extract a comparison key from each element in the array. 
# To support searching complex records, 
# the key function is not applied to the x value.
```






