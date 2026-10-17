# 一回の更新が定数時間でできる (N <= 3000)


def section_DP(N, A):
    dp = [[0] * N for _ in range(N)]
    for l in range(N - 1, -1, -1):
        for r in range(l + 1, N):
            cost = 0
            dp[l][r] = dp[l + 1][r - 1] + cost
            for k in range(l + 1, r):
                dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r])
    return dp


# 一回の更新がNに比例する (N <= 500)


def section_DP(N, A):
    dp = [[0] * N for _ in range(N)]
    for l in range(N - 1, -1, -1):
        for r in range(l + 1, N):
            cost = 0
            dp[l][r] = min(
                dp[l + 1][r] + cost, dp[l + 1][r] + cost, dp[l][r + 1] + cost
            )
    return dp
