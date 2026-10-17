import itertools
import operator
import numpy as np

l = []

# 累積和
print(itertools.accumulate(l))
# 累積最大値
print(list(itertools.accumulate(l, func=max)))
# 累積積
print(list(itertools.accumulate(l, func=operator.mul)))

# 二次元累積和
print(np.cumsum(l, axis=0))

H, W = 0, 0
grid = []
# ヨコに累積和
for i in range(H):
    for j in range(W):
        if i >= 0:
            grid[i][j] += grid[i - 1][j]
# タテに累積和
for i in range(H):
    for j in range(W):
        if j >= 0:
            grid[i][j] += grid[i][j - 1]
