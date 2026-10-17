import heapq


def solve_constrained_shortest_path(graph, N, C, start, end):
    """
    制約付き最短路問題（最大C回休憩可能）を頂点倍加で解く。
    :param graph: 元のグラフ adj[u] = list of (v, weight)
    :param N: 元のノード数
    :param C: 最大休憩回数
    :param start: 始点
    :param end: 終点
    :return: 最小コスト
    """

    # 距離テーブル: dist[node_id][state_index]
    # state_index は休憩回数 (0 から C)
    dist = [[float("inf")] * (C + 1) for _ in range(N)]

    # 優先度付きキュー: (cost, current_node, current_break_count)
    # 拡張されたノード (current_node, current_break_count) を扱う
    pq = [(0, start, 0)]
    dist[start][0] = 0

    while pq:
        current_cost, u, i = heapq.heappop(pq)  # i は休憩回数

        if current_cost > dist[u][i]:
            continue

        for v, weight in graph[u]:
            # 1. 通常移動（休憩しない）: 状態 i は維持
            new_cost_normal = current_cost + weight
            j = i  # 遷移後の休憩回数

            if new_cost_normal < dist[v][j]:
                dist[v][j] = new_cost_normal
                heapq.heappush(pq, (new_cost_normal, v, j))

            # 2. 休憩を伴う移動: 状態 i が i+1 に遷移（休憩回数が増加）
            # (ここでは、休憩コスト w_break = 0 と仮定。もしあれば加算する)
            if i < C:
                new_cost_break = current_cost + weight  # + w_break
                j_break = i + 1  # 遷移後の休憩回数

                if new_cost_break < dist[v][j_break]:
                    dist[v][j_break] = new_cost_break
                    heapq.heappush(pq, (new_cost_break, v, j_break))

    # 終点 end に、任意の休憩回数 j (0 から C) で到達した最短路の中から最小値を選ぶ
    return min(dist[end])
