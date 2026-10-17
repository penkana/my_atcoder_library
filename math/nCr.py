def prepare(n, mod=10**9 + 7):
    n1 = [1] * (n + 1)
    for i in range(2, n + 1):
        n1[i] = (n1[i - 1] * i) % mod
    n2 = [1] * (n + 1)
    for i in range(2, n + 1):
        n2[i] = pow(n1[i], mod - 2, mod)
    return n1, n2


def comb(N, R, n1, n2, mod=10**9 + 7):
    return (n1[N] * (n2[N - R] * n2[R]) % mod) % mod


###

from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under
