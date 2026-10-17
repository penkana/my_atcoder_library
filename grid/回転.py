import math


def rotate_point(x, y, angle):
    # 角度をラジアンに変換
    theta = math.radians(angle)
    # 回転行列の適用
    x_new = x * math.cos(theta) - y * math.sin(theta)
    y_new = x * math.sin(theta) + y * math.cos(theta)
    return x_new, y_new
