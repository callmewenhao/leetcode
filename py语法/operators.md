# 运算符

## := 海象运算符

类似于 C++ 在条件判断中定义变量

```python
if (n := len(ts)) > 2:
    ts.sort()
    for i in range(n - 2):  # 使用前面定义的变量，不必再次调用 len()
        if ts[i + 2] - ts[i] <= 60:
            ans.append(name)
            break
```

