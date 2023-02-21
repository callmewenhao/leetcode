# defaultdict

> 返回一个新的类似字典的对象。 [defaultdict](https://docs.python.org/zh-cn/3/library/collections.html#collections.defaultdict) 是内置 [dict](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict) 类的子类。 它重载了一个方法并添加了一个可写的实例变量。 其余的功能与 dict 类相同因而不在此文档中写明。

## 初始化

```python
d = defaultdict(list)  # 字典值是列表
d[k].append(v)  # 给指定的 key，添加 val

d = defaultdict(int)  # 字典值是数字
d[k] += 1  # 更新计数器的值

d = defaultdict(set)  # 字典值是一个去重集合
d[k].add(v)  # 向集合中添加元素
```

## 遍历元素 .items()

```python
for k, v in d.items():
    ...
```

