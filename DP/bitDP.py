# 区間スケジューリング


def bit_dp(n, dist):
    # dp[S][v]: 訪問済み集合がSで、現在地がvであるときの最小コスト
    unit = float("inf")
    func = min

    dp = [[unit] * n for _ in range(1 << n)]
    # 初期状態：都市0から出発する場合
    dp[1 << 0][0] = 0

    # 集合のサイズが小さい順に更新
    for s in range(1, 1 << n):
        for v in range(n):
            if dp[s][v] == unit:
                continue

            # 次に移動する都市 u を探す
            for u in range(n):
                if not (s >> u) & 1:  # まだ訪問していない場合
                    next_s = s | (1 << u)
                    new_dist = dp[s][v] + dist[v][u]
                    dp[next_s][u] = func(dp[next_s][u], new_dist)

    # すべての都市を訪問し、最後に始点に戻るコストを確認
    res = unit
    full_set = (1 << n) - 1

    # 巡回するとき
    # for v in range(n):
    # res = func(res, dp[full_set][v] + dist[v][0])

    # 巡回しない時
    res = func(dp[full_set])

    return res


N, K, dp, cost = 0, 0, [], []

# 集合DP
for i in range(1, K + 1):
    for j in range(1, 2**N):
        k = j
        while True:
            if k == 0:
                break
            dp[i][j] = min(dp[i][j], max(dp[i - 1][j - k], cost[k]))
            k = (k - 1) & j
print(dp[K][-1])
