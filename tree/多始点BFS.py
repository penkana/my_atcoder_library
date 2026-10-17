from collections import deque


# 隣接リスト
def multi_source_bfs(graph, starts):
    # 距離を管理する辞書（未訪問のノードは-1）
    distances = {node: -1 for node in graph}
    queue = deque()

    # すべての始点をキューに投入し、距離を 0 に設定する
    for src in starts:
        if src in distances:
            distances[src] = 0
            queue.append(src)

    # 探索の開始
    while queue:
        current = queue.popleft()

        # 現在のノードに隣接するノードを巡回
        for neighbor in graph[current]:
            # 未訪問のノードである場合のみ更新
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return distances


# グリッド
from collections import deque


def multi_source_bfs_grid(grid, starts):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # 距離を管理する2次元配列を -1 で初期化
    distances = [[-1] * cols for _ in range(rows)]

    queue = deque()

    # すべての始点をキューに投入し、距離を 0 に設定
    for r, c in starts:
        # グリッドの範囲内であり、かつ壁ではない場合のみ処理
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] != 1:
            distances[r][c] = 0
            queue.append((r, c))

    # 上下左右の移動ベクトル
    dx, d = [0, 1, 0, -1, 0], 4  # 上下左右
    dx, d = [1, 0, -1, 0, 1, -1, -1, 1, 1], 8  # 上下左右斜め

    # 探索の開始
    while queue:
        r, c = queue.popleft()

        # 隣接する4方向を走査
        for i in range(d):
            nr, nc = r + dx[i], c + dx[i + 1]

            # グリッドの範囲内かどうかの判定
            if 0 <= nr < rows and 0 <= nc < cols:
                # 壁ではなく、かつ未訪問（距離が -1）の場合
                if grid[nr][nc] != 1 and distances[nr][nc] == -1:
                    distances[nr][nc] = distances[r][c] + 1
                    queue.append((nr, nc))

    return distances
