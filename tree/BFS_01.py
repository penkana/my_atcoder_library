from collections import deque


def BFS_01(grid, start, goal, H, W):
    # 最短距離をメモする変数
    memo = [[-1] * W for _ in range(H)]

    # スタートを0に
    memo[start[0]][start[1]] = 0

    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # スタートを最初に挿入
    q = deque([start])  # キュー：[(0, 0)]
    while q:
        i, j = q.popleft()  # キューの左から見る
        for d in dir:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < H and 0 <= nj < W:  # 添え字が不正でない
                if grid[ni][nj] == "#":
                    continue  # 壁
                if memo[ni][nj] != -1:
                    continue  # 確定済み
                # コストを計算
                cost = 1 if grid[ni][nj] == "*" else 0
                # 次の要素のコストをメモ
                memo[ni][nj] = memo[i][j] + cost

                # コストに応じて追加
                if cost == 1:  # コストが1の場合
                    q.append((ni, nj))  # 右に追加
                else:  # コストが0の場合
                    q.appendleft((ni, nj))  # 左に追加

    return memo[goal[0]][goal[1]]


# 入力
H, W = map(int, input().split())
S = [input() for _ in range(H)]

# スタートとゴールを設定
s, g = (0, 0), (H - 1, W - 1)
