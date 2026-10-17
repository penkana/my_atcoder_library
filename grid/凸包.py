from collections import deque


def get_convex(points):
    n = len(points)
    if n <= 2:
        return points

    # x座標、次にy座標で昇順ソート
    points.sort()

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # 下部凸包の構築
    lower = deque([])
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    lower.pop()

    # 上部凸包の構築
    upper = deque([])
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    upper.pop()

    # 重複する端点を除いて結合
    return list(lower) + list(upper)
