# DAGの場合
from collections import deque

# in_degreehは入次数で、ある頂点に入ってくる辺の本数
# グラフは0-indexed


def topological_sort(graph, in_degree, N):
    # 入次数が0の頂点をキューに追加
    queue = deque([i for i, deg in enumerate(in_degree) if deg == 0])

    # 入次数が0の頂点から探索する
    result = []
    parent = [-1] * N
    while queue:
        now = queue.popleft()
        result.append(now)
        for i in graph[now]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)
                parent[i] = now

    return result, parent


def calculate_subtree_sizes(graph, in_degree, N):
    subtree_size = [1] * N
    result, parent = topological_sort(graph, in_degree, N)

    for curr in reversed(result):
        p = parent[curr]
        if p != -1:
            subtree_size[p] += subtree_size[curr]

    return subtree_size


# DAGではない場合

import sys

# 再帰回数の上限を増やす（深い木の場合に必要）
sys.setrecursionlimit(200000)


def count_subtree_sizes(n, adj, root=0):
    size = [0] * n

    def dfs(curr, prev):
        count = 1  # 自分自身をカウント
        for neighbor in adj[curr]:
            if neighbor != prev:  # 親に戻らないようにする
                count += dfs(neighbor, curr)
        size[curr] = count
        return count

    dfs(root, -1)
    return size
