# 隣接リストダイクストラ
import heapq


def dijkstra(graph, start, end, N):
    distances = [float("infinity")] * N
    distances[start] = 0
    prev = [-1] * N
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            root = [end]
            while root[-1] != start:
                root.append(prev[root[-1]])
            return distances[end], root[::-1]

        if distances[current_node] < current_distance:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                prev[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return None, None


# グラフの定義
graph = [
    [[1, 4], [2, 3]],  # ← 頂点Aからの辺のリスト
    [[2, 1], [3, 1], [4, 5]],  # ← 頂点Bからの辺のリスト
    [[5, 2]],  # ← 頂点Cからの辺のリスト
    [[4, 3]],  # ← 頂点Dからの辺のリスト
    [[6, 2]],  # ← 頂点Eからの辺のリスト
    [[4, 1], [6, 4]],  # ← 頂点Fからの辺のリスト
    [],  # ← 頂点Gからの辺のリスト
]
N = 7

cost, root = dijkstra(graph, 0, 6, N)


# グリッドダイクストラ
import heapq


def dijkstra_2d(grid, start, end, H, W):
    """二次元グリッド（迷路）に対するダイクストラ法

    :param grid: リストのリスト（例: [['.', '.', '#'], ['.', '#', '.'], ['.', '.',
    '.']]）
    :param start: スタート座標のタプル (start_r, start_c)
    :param end: ゴール座標のタプル (end_r, end_c)
    :return: (最短距離, 経路の座標リスト)。到達不能な場合は (None, None)
    """
    # 1. 距離配列と経路復元用配列を二次元で初期化
    distances = [[float("infinity")] * W for _ in range(H)]
    start_r, start_c = start
    distances[start_r][start_c] = 0

    prev = [[None] * W for _ in range(H)]

    # キューには (現在の距離, (現在の行, 現在の列)) を格納
    queue = [(0, start)]

    # 上下左右の移動ベクトル
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        current_distance, (cr, cc) = heapq.heappop(queue)

        # ゴールに到達した場合、経路を復元して返す
        if (cr, cc) == end:
            path = [end]
            while path[-1] != start:
                path.append(prev[path[-1][0]][path[-1][1]])
            return distances[end[0]][end[1]], path[::-1]

        # 既により短い経路が見つかっている場合はスキップ
        if distances[cr][cc] < current_distance:
            continue

        # 2. 隣接する4方向のマスを探索
        for dr, dc in DIRECTIONS:
            nr, nc = cr + dr, cc + dc

            # 3. 境界条件のチェック
            if not (0 <= nr < H and 0 <= nc < W):
                continue

            # 壁（#）の場合は通行不可
            if grid[nr][nc] == "#":
                continue

            # グリッドの移動コストは一律 1 と仮定
            weight = 1
            distance = current_distance + weight

            # コスト更新処理
            if distance < distances[nr][nc]:
                distances[nr][nc] = distance
                prev[nr][nc] = (cr, cc)
                heapq.heappush(queue, (distance, (nr, nc)))

    return None, None
