import math

l = [27, 18, 9, 3]
A, B = 1, 1


# 最大公約数
print(math.gcd(6, 4))
print(math.gcd(*l))
# 最小公倍数
print(math.lcm(6, 4))
print(math.lcm(*l))
# 逆元
n = 1
MOD = 1
pow(n, -1, MOD)
# 切り上げ
print((A + B - 1) // B)
print((A + 1) // 1)


def custom_ceil(n):
    if n == int(n):
        return int(n)
    else:
        return int(n) + 1


# 切り捨て
print(A // B)
print(int(A))


deg = 180
rad = math.pi
# 度をラジアンに変換
rad_value = math.radians(deg)
# ラジアンを度に変換
deg_value = math.degrees(rad_value)


# 偏角
def calc_deg(X0, Y0, X1, Y1):
    rad = math.degrees(math.atan2(Y1 - Y0, X1 - X0))
    if rad >= 0:
        return rad
    else:
        return 360 + rad


# ユークリッド距離
a, b = (0, 0), (1, 1)
print(math.dist(a, b))

# リスト内要素の積
print(math.prod(a))
