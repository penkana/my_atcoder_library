grid = [[]]

x, y = 0, 0
dx, d = [0, 1, 0, -1, 0], 4  # 上下左右
dx, d = [1, 0, -1, 0, 1, -1, -1, 1, 1], 8  # 上下左右斜め
# 現在 x, y にいるとして
for i in range(d):
    print(grid[x + dx[i]][y + dx[i + 1]])
