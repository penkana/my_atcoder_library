# 二次元
N = 100
imos = [[0] * N for _ in range(N)]
for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    imos[ly][lx] += 1
    imos[ry][rx] += 1
    imos[ry][lx] -= 1
    imos[ly][rx] -= 1
for i in range(N - 1):
    for j in range(N - 1):
        imos[i + 1][j] += imos[i][j]
        imos[i][j + 1] += imos[i][j]
        imos[i + 1][j + 1] -= imos[i][j]
