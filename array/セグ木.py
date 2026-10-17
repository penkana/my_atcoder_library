# 非再帰によるセグメント木の実装（1-indexed)


class SegmentTree:
    def __init__(self, data, func, unit):
        n = len(data)
        self.n = n
        self.func = func
        self.unit = unit
        self.tree = [unit] * (2 * n)

        tree = self.tree
        # 葉の構築
        for i in range(n):
            tree[i + n] = data[i]
        # 内部ノードの構築
        for i in range(n - 1, 0, -1):
            tree[i] = func(tree[i << 1], tree[i << 1 | 1])

    def update(self, i, val):
        # ローカル変数にして高速化
        tree = self.tree
        func = self.func

        i += self.n
        tree[i] = val
        while i > 1:
            # 親へ移動し、その都度左右の子を合成
            i >>= 1  # i//2
            tree[i] = func(tree[i << 1], tree[i << 1 | 1])

    def query(self, left, right):
        # ローカル変数にして高速化
        res = self.unit
        tree = self.tree
        func = self.func

        left += self.n
        right += self.n

        while left < right:
            if left & 1:  # i % 2 == 1
                res = func(res, tree[left])
                left += 1
            if right & 1:
                right -= 1
                res = func(res, tree[right])
            left >>= 1
            right >>= 1
        return res


# 使用例

data = []

# 集約演算（和）と単位元（0）

# 区間和
op = lambda a, b: a + b
unit = 0
# 区間最小値
op = lambda a, b: min(a, b)
unit = float("inf")
# 区間最大値
op = lambda a, b: max(a, b)
unit = float("-inf")

st = SegmentTree(data, op, unit)

# 要素の更新: data[2] = 2 を 10 に更新
st.update(2, 10)

print(st.query(0, 6))  # 区間和
