# str

> `str` 是内建数据类型 [文档](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
> 
> 可以把 python 中的字符串理解为一个 `str` 类的对象
> 字符串具有该类的很多方法
> 
> 补充两个常用的内置方法 
> 
> chr() 把 ASCII 码值转成字符 && 
> ord() 把 字符转成 ASCII 码值

## 字符重复次数

`ch * n` 表示字符 ch 重复 n 次

## 字符串排序

python 中没有直接对字符串排序的方法。
一般是使用 sorted() 函数，得到一个排序后的字 list 然后使用 join 拼接

## 反转 str

反转字符串只能用切片 `s = s[::-1] or s[l:r] = s[l:r][::-1]` 
或者 把字符串转成 `list` 使用 `reverse()` 最后 `join()` 起来

## count()

Return the number of non-overlapping occurrences of substring sub in the range [start, end].
Optional arguments start and end are interpreted as in slice notation.

```python
s = "hello, world!"
print(s.count(''))  # 长度+1
print(s.count('l'))  # l 的个数 3
print(s.count('l', 0, 5))  # l 的个数 2
```

## find()

Return the lowest index in the string where substring sub is found within the slice s[start:end]. 
Optional arguments start and end are interpreted as in slice notation. 
Return -1 if sub is not found.

> Note The find() method should be used only if you need to know the position of sub. 
> To check if sub is a substring or not, use the in operator:
> ```python
> >>> 'Py' in 'Python'
> True
> ```

## isXXX()

> 判断 str 对象是否是某种字符
> 
> isalnum() isalpha() isascii() isdecimal() isdigit() 
> 
> islower() isnumeric() isspace() istitle() isupper()

## replace()

**定义和用法：**
`replace()` 方法用另一个指定的短语替换一个指定的短语。
返回一个新的字符串，原字符串不变 🤗

注释：如果未指定其他内容，则将替换所有出现的指定短语。

`string.replace(oldvalue, newvalue, count)`

| parameters | Description                   |
|------------|-------------------------------|
| oldvalue   | 必需。要检索的字符串。                   |
| newvalue   | 必需。替换旧值的字符串。                  |
| count      | 可选。数字，指定要替换的旧值出现次数。**默认为所有的出现。**  |

## join()

字符串拼接

## lower() upper()

返回小/大写

## split()

切片函数

## strip()

删去某些字符


