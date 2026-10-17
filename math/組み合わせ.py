# 重複組み合わせ(仕切り棒)
## 上限がある時
## もともと全部の箱に上限まで入っていて、超過分を抜き出すと考える。
## または、どれかの箱に上限+1あり、残りをさらに分配すると考える包徐原理

from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def f_H(n, r):
    return cmb(n + r - 1, r)


n, r = 0, 0

"""
(例)200個の区別のないボールを、A,B,Cの3箱に入れる。ただし、それぞれの箱にボールは100個までしか入らない。ボールの入れ方は何通りか。
"""
ans = f_H(3, 200) - 3 * f_H(3, 99)
