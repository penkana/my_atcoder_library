# 二項係数
class Comb:

    def __init__(self, maxn, mod):
        self.fact = [0] * (maxn + 1)
        self.inv = [0] * (maxn + 1)
        self.finv = [0] * (maxn + 1)

        self.mod = mod

        self.fact[0], self.fact[1] = 1, 1
        self.inv[1] = 1
        self.finv[0], self.finv[1] = 1, 1

        for i in range(2, maxn + 1):
            self.fact[i] = (self.fact[i - 1] * i) % mod
            self.inv[i] = mod - ((self.inv[mod % i] * (mod // i)) % mod)
            self.finv[i] = (self.finv[i - 1] * self.inv[i]) % mod

    def calc(self, n, k):
        return (self.fact[n] * self.finv[k] * self.finv[n - k]) % self.mod


# 定数設定
MAX_N = 10**5  # N の最大値
MOD = 10**9 + 7  # 法とする素数（非常に大きな素数）

C = Comb(MAX_N, MOD)

n_b, k_b = 100000, 50000
result_b = C.calc(n_b, k_b)
