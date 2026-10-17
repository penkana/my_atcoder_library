import sys

sys.setrecursionlimit(10**6)


def extended_euclid(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        g, xd, yd = extended_euclid(b, a % b)
        return (g, yd, xd - a // b * yd)


# ax + by = gcd(a,b)　の解 (ax' + by' = 1)

import math


def solve_coin_problem_sympy(A, B, C, N):
    coins = sorted([A, B, C], reverse=True)
    A, B, C = coins[0], coins[1], coins[2]

    x_prime, y_prime, gcd_bc = extended_euclid(B, C)

    min_coins = float("inf")

    for x in range(N // A, -1, -1):
        rem = N - A * x
        if rem % gcd_bc != 0:
            continue

        # By + Cz = rem の特殊解を求める
        k = rem // gcd_bc
        y_special = x_prime * k
        z_special = y_prime * k

        # 非負整数解を探す
        # 一般解: y = y_special + t * (C / gcd_bc), z = z_special - t * (B / gcd_bc)
        # y >= 0 かつ z >= 0 となるtの範囲を求める
        term_y = C // gcd_bc
        term_z = B // gcd_bc

        # y >= 0 より y_special + t * term_y >= 0 -> t >= -y_special / term_y
        min_t_y = math.ceil(-y_special / term_y)

        # z >= 0 より z_special - t * term_z >= 0 -> t <= z_special / term_z
        max_t_z = math.floor(z_special / term_z)

        # 非負整数解が存在しない場合
        if min_t_y > max_t_z:
            continue

        # y+zが最小となるtを探す
        # y+z = (y_special + z_special) + t * (term_y - term_z)
        # term_y と term_z の大小関係でtの最適な値が変わる
        if term_y - term_z > 0:
            optimal_t = min_t_y
        else:
            optimal_t = max_t_z

        # 最小枚数を計算
        y = y_special + optimal_t * term_y
        z = z_special - optimal_t * term_z

        total_coins = x + y + z
        min_coins = min(min_coins, total_coins)

    return min_coins if min_coins != float("inf") else -1
