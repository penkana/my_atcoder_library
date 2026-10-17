class LazySegmentTree:
    def __init__(self, data, func, mapping, composition, unit, lazy_unit):
        n_orig = len(data)
        self.h = (n_orig - 1).bit_length()
        self.n = 1 << self.h

        self.func = func  # 更新関数
        self.mapping = mapping  # 遅延値の適用関数
        self.composition = composition  # 既存遅延値の操作
        self.unit = unit
        self.lazy_unit = lazy_unit

        # 配列の初期化
        self.tree = [unit] * (2 * self.n)
        self.lazy = [lazy_unit] * self.n

        # sz_table の事前計算
        # 各ノードがカバーする範囲の大きさを保持
        self.sz_table = [0] * (2 * self.n)
        for i in range(1, 2 * self.n):
            self.sz_table[i] = 1 << (self.h - (i.bit_length() - 1))

        # 属性参照を減らすためのローカル変数化
        tree = self.tree
        for i in range(n_orig):
            tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            tree[i] = func(tree[i << 1], tree[i << 1 | 1])

    def _apply(self, i, f, tree, lazy, sz_table):
        # 遅延値の適用
        tree[i] = self.mapping(f, tree[i], sz_table[i])
        if i < self.n:
            lazy[i] = self.composition(f, lazy[i])

    def _push(self, i, tree, lazy, sz_table):
        # 上から下への伝播
        f = lazy[i]
        if f == self.lazy_unit:
            return
        self._apply(i << 1, f, tree, lazy, sz_table)
        self._apply(i << 1 | 1, f, tree, lazy, sz_table)
        lazy[i] = self.lazy_unit

    def _build(self, i, tree, lazy, sz_table):
        # 下から上への再計算
        res = self.func(tree[i << 1], tree[i << 1 | 1])
        tree[i] = self.mapping(lazy[i], res, sz_table[i])

    def update(self, l, r, f):
        # 半区間更新
        n = self.n
        tree = self.tree
        lazy = self.lazy
        sz_table = self.sz_table

        l += n
        r += n
        l0, r0 = l, r

        # 上から下へ伝播 (push)
        for s in range(self.h, 0, -1):
            if ((l0 >> s) << s) != l0:
                self._push(l0 >> s, tree, lazy, sz_table)
            if ((r0 >> s) << s) != r0:
                self._push((r0 - 1) >> s, tree, lazy, sz_table)

        # 区間更新
        while l < r:
            if l & 1:
                self._apply(l, f, tree, lazy, sz_table)
                l += 1
            if r & 1:
                r -= 1
                self._apply(r, f, tree, lazy, sz_table)
            l >>= 1
            r >>= 1

        # 下から上へ再計算 (build)
        l, r = l0, r0
        for s in range(1, self.h + 1):
            if ((l >> s) << s) != l:
                self._build(l >> s, tree, lazy, sz_table)
            if ((r >> s) << s) != r:
                self._build((r - 1) >> s, tree, lazy, sz_table)

    def query(self, l, r):
        # 半区間クエリ
        n = self.n
        tree = self.tree
        lazy = self.lazy
        sz_table = self.sz_table

        l += n
        r += n

        # 必要な経路のみ push
        for s in range(self.h, 0, -1):
            if ((l >> s) << s) != l:
                self._push(l >> s, tree, lazy, sz_table)
            if ((r >> s) << s) != r:
                self._push((r - 1) >> s, tree, lazy, sz_table)

        res = self.unit
        while l < r:
            if l & 1:
                res = self.func(res, tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.func(res, tree[r])
            l >>= 1
            r >>= 1
        return res


# 区間加算・区間最小値
func = lambda x, y: min(x, y)
mapping = lambda f, x, sz: f + x  # szは未使用
composition = lambda f, g: f + g
unit = float("inf")
lazy_unit = 0

# 区間加算・区間和
func = lambda x, y: x + y
mapping = lambda f, x, sz: x + f * sz
composition = lambda f, g: f + g
unit = 0
lazy_unit = 0

# 区間更新・区間最小値
func = lambda x, y: min(x, y)
mapping = lambda f, x, sz: f if f is not None else x
composition = lambda f, g: f if f is not None else g
unit = float("inf")
lazy_unit = None

# 区間更新・区間和
func = lambda x, y: x + y
mapping = lambda f, x, sz: f * sz if f is not None else x
composition = lambda f, g: f if f is not None else g
unit = 0
lazy_unit = None

# 区間線形変換(ax+bに置き換える)・区間和
MOD = 10**9 + 7
func = lambda x, y: (x + y) % MOD
mapping = lambda f, x, sz: (f[0] * x + f[1] * sz) % MOD
composition = lambda f, g: (f[0] * g[0] % MOD, (f[0] * g[1] + f[1]) % MOD)
unit = 0
lazy_unit = (1, 0)
