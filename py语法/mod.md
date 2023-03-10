# MOD

> Python 取模运算会保证结果非负。

如果 x 和 y 均为非负数，
则 x 同余 y 相当于 `x mod p == y mod p` <= `(x-y) mod p`

如果 x<0，y≥0，
则 x 同余 y 相当于 `x mod p + p == y mod p` <= `(x-y) mod p`

例如 −17 mod 10 + 10 = −7 + 10 = 3

为了避免判断 x 是否为负数，等号左边可以写成 `(x mod p + p) mod p`

这样无论 x 是否为负数，最终都会落在区间 [0,p) 中。