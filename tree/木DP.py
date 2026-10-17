def tree_dp(unit, root, graph, N):
    merge = lambda x, y: max(x, y)
    add = lambda x: x + 1

    # BFSでトポロジカルソート
    order = [root]
    parent = [-1] * N
    idx = 0
    while idx < len(order):
        u = order[idx]
        idx += 1
        for v in graph[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            order.append(v)

    # 木DP
    dp = [unit] * N

    for i in reversed(order):
        res = unit
        for j in graph[i]:
            if j == parent[i]:
                continue
            res = merge(res, dp[j])
        dp[i] = add(res)

    return dp[root]
