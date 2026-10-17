from collections import deque

# in_degreehは入次数で、ある頂点に入ってくる辺の本数
# グラフは0-indexed


def topological_sort(graph, in_degree):
    # 入次数が0の頂点をキューに追加
    queue = deque([i for i, deg in enumerate(in_degree) if deg == 0])

    # 入次数が0の頂点から探索する
    result = []
    while queue:
        now = queue.popleft()
        result.append(now)
        for i in graph[now]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)

    return result
