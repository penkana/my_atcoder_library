from itertools import accumulate


def rerooting_dp(unit, graph, N, root=0):
    fix = max
    merge = lambda x: fix(x)
    adj_bu = lambda x: x + 1
    adj_td = lambda x: x + 1

    # BFSでトポロジカルソート
    order = [root]
    parent = [-1] * N
    child = [[] for _ in range(N)]
    idx = 0
    while idx < len(order):
        u = order[idx]
        idx += 1
        for v in graph[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            child[u].append(v)
            order.append(v)

    # dp[u][v] = 有向辺 u -> v に載せる値
    dp = [{v: unit for v in u} for u in graph]

    # ボトムアップ
    for u in reversed(order):
        par = parent[u]
        if par == -1:
            continue
        res = unit
        for c in child[u]:
            res = merge([res, dp[c][u]])
        dp[u][par] = adj_bu(res)

    # 累積
    prefix = [[] for _ in range(N)]
    suffix = [[] for _ in range(N)]
    for u in range(N):
        values = [dp[v][u] for v in child[u]]
        prefix[u] = [0] + list(accumulate(values, fix))
        suffix[u] = list(accumulate(reversed(values), fix))[::-1] + [0]

    # トップダウン
    for u in order:
        par = parent[u]
        par_in = dp[par][u] if par != -1 else 0
        for i, v in enumerate(child[u]):
            dp[u][v] = adj_td(merge([par_in, prefix[u][i], suffix[u][i + 1]]))

    ans = [merge(dp[x][v] for x in graph[v]) for v in range(N)]
    return ans
