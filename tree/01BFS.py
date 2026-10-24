# 参考元：https://qiita.com/yuu_kyopro/items/761919d9bccc88521863

from collections import deque

V = 0  # 頂点数
goal = 1
G = []

dist = [10**6] * (V + 1)
dq = deque()
dq.append((1, 0))
while dq:
    # コストが最小の頂点を取り出す
    cost, v = dq.popleft()
    if v == goal:
        break
    if dist[v] < cost:
        continue
    for k in range(len(G[v])):
        next_v = G[v][k]
        next_cost = 0 if k == 0 else 1
        if dist[next_v] > cost + next_cost:
            dist[next_v] = cost + next_cost
            if next_cost == 1:  # コストが増えるなら
                dq.append((cost + next_cost, next_v))
            elif next_cost == 0:
                dq.appendleft((cost + next_cost, next_v))
