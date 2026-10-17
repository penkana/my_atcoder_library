import sys

# 再帰上限を増やす（深いゲーム木の場合）
sys.setrecursionlimit(200000)


def mex(s):
    # 集合 s に含まれない最小の非負整数を返す
    m = 0
    while m in s:
        m += 1
    return m


memo = {}


def get_grundy(n):
    if n in memo:
        return memo[n]

    # 終了条件
    if n == 0:
        return 0

    # 次の状態のGrundy数を集める
    next_grundys = set()

    # 例：1, 2, 3個取れるゲームの場合
    for i in [1, 2, 3]:
        if n - i >= 0:
            next_grundys.add(get_grundy(n - i))

    res = mex(next_grundys)
    memo[n] = res
    return res


# 複数の山がある時は、各結果のxor和が0でなければ先手必勝
