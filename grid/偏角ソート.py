from functools import cmp_to_key


def angle_sort(points, center=(0, 0), start=(0, 1), clockwise=True, reverse_dist=False):
    cx, cy = center
    sx, sy = start[0] - cx, start[1] - cy

    # startベクトルが(0,0)の場合はデフォルトの上向きにする
    if sx == 0 and sy == 0:
        sx, sy = 0, 1

    def get_region(x, y):
        # 外積: v_ref × v
        cross = sx * y - sy * x
        if cross > 0:  # 反時計回りに0-180度の範囲
            return 0 if not clockwise else 1
        if cross < 0:  # 180-360度の範囲
            return 1 if not clockwise else 0

        # 外積が0（同一直線上）の場合、内積で前後を判定
        dot = sx * x + sy * y
        if dot >= 0:  # 同じ方向
            return 0
        else:  # 真逆の方向
            return 1

    def compare(p1, p2):
        x1, y1 = p1[0] - cx, p1[1] - cy
        x2, y2 = p2[0] - cx, p2[1] - cy

        # 領域判定
        reg1 = get_region(x1, y1)
        reg2 = get_region(x2, y2)
        if reg1 != reg2:
            return reg1 - reg2

        # 外積による偏角比較
        cross = x1 * y2 - x2 * y1
        if cross != 0:
            if clockwise:
                return 1 if cross > 0 else -1
            else:
                return -1 if cross > 0 else 1

        # 同一偏角時の距離比較
        dist1 = x1**2 + y1**2
        dist2 = x2**2 + y2**2

        if dist1 == dist2:
            return 0

        # 通常は昇順（近い順）、reverse_dist=Trueで降順（遠い順）
        if not reverse_dist:
            return 1 if dist1 > dist2 else -1
        else:
            return -1 if dist1 > dist2 else 1

    return sorted(points, key=cmp_to_key(compare))


# --- 使用例 ---
p = [(0, 2), (2, 0), (0, -2), (-2, 0), (1, 1), (-1, -1)]

# 12時方向から時計回り
result = angle_sort(p, center=(0, 0), start=(0, 1), clockwise=True)
print(f"時計回り: {result}")
