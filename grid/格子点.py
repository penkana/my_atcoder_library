# ピックの定理
# 多角形の頂点が全て格子点上の時 かつ　単純多角形（自己交差なし）のとき、面積から逆算
# Area = I + B/2 - 1 (Area:面積,I:内部に格子点数,B:辺上にある格子点数)
# I = Area - B/2 + 1
# B:各辺(x1,y1),(x2,y2)において辺上の格子点数はgcd(|x1-x2|,|y1-y2|)

import math


def count_points(vertices):
    n = len(vertices)
    area_2 = 0  # 面積の2倍
    b = 0  # 辺上の格子点数

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # 次の頂点（最後は最初に戻る）
        # 靴紐の公式で面積を計算
        area_2 += x1 * y2 - x2 * y1
        # 辺上の格子点数を計算
        b += math.gcd(abs(x2 - x1), abs(y2 - y1))

    # ピックの定理
    i_points = (abs(area_2) - b + 2) // 2

    return i_points, int(b)


# 使用例: (0,0), (3,0), (0,3) の直角三角形
pts = [(0, 0), (3, 0), (0, 3)]
inner, boundary = count_points(pts)

print(f"内部の格子点数: {inner}")
print(f"辺上の格子点数: {boundary}")
print(f"合計の格子点数: {inner + boundary}")
