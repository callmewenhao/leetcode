# list 语法技巧

## 多维 list 多维排序

```python
# 二维数组
a = [[1, 2], [2, 3], [100, -1], [2, -1], [1, 100]]
print(sorted(a, key=lambda x:(x[0], x[1])))  # 先第1维升序 再第2维升序
# [[1, 2], [1, 100], [2, -1], [2, 3], [100, -1], [100, 100]]
print(sorted(a, key=lambda x:(x[0], -x[1])))  # 先第1维升序 再第2维降序
# [[1, 100], [1, 2], [2, 3], [2, -1], [100, 100], [100, -1]]
print(sorted(a, key=lambda x:(x[1], x[0])))  # 先第2维升序 再第1维升序
# [[2, -1], [100, -1], [1, 2], [2, 3], [1, 100], [100, 100]]
```

## 一维 二维 list 初始化

```python
# 一维
a = [0] * 10  # 长度为10，值为0
b = [[0] * 10 for _ in range(20)] # 长度为20 x 10，值为0
# 注意：[[0] * 10] * 20 是不对的初始化方式
```

## 列表推导式

```python
# code
l = [val ** 2 for val in range(10) if val % 2 == 0]
print(l)
s = sum(val ** 2 for val in range(10) if val % 2 == 0)
print(s)
# output
[0, 4, 16, 36, 64]
120
```

## zip() 来组合列表

```python
ans = 0
for h, p, s in zip(height, pre_max, suf_max):
    ans += min(p, s) - h
return ans
```

## 切片操作颠倒列表 [::-1]

```python
original_list = [1, 2, 3, 4, 5]
reversed_list = original_list[::-1]
```

## in 运算符检查元素存在情况

```python
if item in list_name: print(f"{item} is in the list!")
```

## 统计元素出现的次数

```python
aList = [123, 'xyz', 'zara', 'abc', 123];
print
"Count for 123 : ", aList.count(123);
print
"Count for zara : ", aList.count('zara');
```

## 展平嵌套列表

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [i for j in nested_list for i in j]
```

## 借助 set 检查唯一性

```python
l1 = [1, 2, 3, 4, 5]
len(l1) == len(set(l1))  # 相等唯一
```



