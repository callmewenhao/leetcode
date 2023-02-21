# Counter
A Counter is a dict subclass for counting hashable objects. 
It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. 
Counts are allowed to be any integer value including zero or negative counts. 
The Counter class is similar to bags or multisets in other languages.

## 初始化
可以使用字符串、列表、字典等形式

```python
c = Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
c = Counter(cats=4, dogs=8)             # a new counter from keyword args
c = Counter(['eggs', 'ham'])            # a new counter from a list
```

## .items(), .keys(), .values()

```python
l = ["a", "a", "a", "b", "c", "c", "f", "g", "g", "g", "f"]
dic = Counter(l)

print(dic.items())  # dic.items()获取字典的key和value 
# 结果:按字母顺序排序的
#dict_items([('a', 3), ('b', 1), ('c', 2), ('f', 2), ('g', 3)])

print(dic.keys())
#结果:
#dict_keys(['a', 'b', 'c', 'f', 'g'])

print(dic.values())
#结果：
#dict_values([3, 1, 2, 2, 3])
```

## 简单使用
```python
c = Counter()
c['a'] += 1
```









