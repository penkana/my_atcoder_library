# 行きがけ順
def dfs_pre(graph, start_node):
    stack = [(start_node, None)]

    while stack:
        s, parent = stack.pop()
        # ここで処理
        for next in graph[s]:
            if next == parent:
                continue
            stack.append((next, s))
    return


# 帰りがけ順
def dfs_post(graph, start_node):
    visited = {start_node}
    stack = [start_node]
    next_child_idx = {node: 0 for node in graph}
    order = []

    while stack:
        v = stack[-1]
        neighbors = graph[v]

        # 次に訪問できる隣接ノードを探す
        found = False
        while next_child_idx[v] < len(neighbors):
            w = neighbors[next_child_idx[v]]
            next_child_idx[v] += 1

            if w not in visited:
                visited.add(w)
                stack.append(w)
                found = True
                break  # 子ノードへ進む

        if not found:
            # 全ての隣接ノードをチェックし終えたら stack から取り出す
            order.append(stack.pop())

    return order
