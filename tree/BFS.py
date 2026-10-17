from collections import deque

n, m = 0, 0  # nは頂点の数、mは辺の数
graph = []  # 隣接リスト


def bfs(u, graph, n):
    queue = deque([u])
    d = [None] * n  # uからの距離の初期化
    d[u] = 0  # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d


# グリッド
def bfs_grid(start, grid, H, W):
    queue = deque([start])
    distance = [[None] * W for _ in range(H)]  # uからの距離の初期化
    distance[start[0]][start[1]] = 0  # 自分との距離は0
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        h, w = queue.popleft()
        for d in dir:
            nh, nw = h + d[0], w + d[1]
            if 0 <= nh < H and 0 <= nw < W:
                if grid[nh][nw] == "#":
                    continue  # 壁
                distance[nh][nw] = min(distance[nh][nw], distance[h][w] + 1)
                queue.append((nh, nw))
    return d
