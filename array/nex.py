# nex[i][c] ← 文字列 Sの i文字目以降で、文字 cが出現する最小の添字 (存在しない場合は N)

def calc_next(S):
    # 文字列 S の長さ
    N = len(S)

    # 答え
    res = [[N] * 26 for _ in range(N + 1)]

    # 後ろから見る
    for i in range(N - 1, -1, -1):
        # i + 1 文字目以降の結果を一旦 i 文字にコピー
        for j in range(26):
            res[i][j] = res[i + 1][j]

        # i 文字目の情報を反映させる
        res[i][ord(S[i]) - ord('a')] = i

    # 答えを返す
    return res