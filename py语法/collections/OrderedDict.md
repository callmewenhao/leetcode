# OrderedDict

> Return an instance of a dict subclass that has methods specialized for rearranging dictionary order.
> OrderedDict 会根据插入顺序进行排序，同时提供更改顺序的 API

## 初始化

```python
import collections
d = collections.OrderedDict()
d["name"] = "muya"
d["age"] = 25
d["money"] = "Zero"
```

## 常用函数

```python
dic = collections.OrderedDict()

# clear(清空有序字典)
dic.clear()

# items(返回由“键值对组成元素“的列表)
dic.items()
 
# keys(获取字典所有的key)
dic.keys()
 
# values(获取字典所有的value，返回一个列表)
dic.values()
 
# move_to_end(指定一个key，把对应的key-value移到最后)
dic["name"] = "muya"
dic["age"] = 25
dic["money"] = "Zero"
dic.move_to_end("name")    # 将name移到最后
dic.move_to_end("money", last=False)   # 设置last为False, 将money移到最前面
 
# pop(获取指定key的value，并在字典中删除)
dic.pop("name")           # 删除name, 注意必须指定关键字key
 
# popitem(按照后进先出原则，删除最后加入的元素，返回key-value)
dic.popitem()            # 删除最后加入的
dic.popitem(last=False)  # 删除第一个加入的
```

