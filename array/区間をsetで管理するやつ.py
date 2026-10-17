from sortedcontainers import SortedSet


class intervalSet:
    def __init__(self, data, count_tiles, count_sets=1) -> None:
        self.data = SortedSet(data)
        self.count_tiles = count_tiles
        self.count_sets = count_sets

    def update_plas(self, L, R):  # 反転しない
        if len(self.data) < 2:
            return
        left = self.data.bisect_left(L)  # L <= r_i
        left -= left % 2
        left = self.f_plas(L, R, left)
        while left + 1 < len(self.data) and self.data[left] <= R:
            left = self.f_plas(L, R, left)

    def f_plas(self, L, R, left):
        l_i = self.data[left]
        r_i = self.data[left + 1] - 1  # type: ignore

        if r_i < L:
            left += 2
            return left
        if R < l_i:
            left = len(self.data)
            return left

        if l_i < L:
            if r_i <= R:  # l_i < L <= r_i <= R
                self.count_tiles -= r_i + 1 - L
                self.data.remove(r_i + 1)  # [l_i,r_i+1) 削除
                self.data.add(L)  # [l_i,L) 挿入
                left += 2
            else:  # l_i < L and R <= r_i
                # [l_i,r_i+1) 削除
                self.count_tiles -= R - L + 1
                self.count_sets += 1
                self.data.add(L)  # [l_i,L) 挿入
                self.data.add(R + 1)  # [R+1,r_i+1) 挿入
                left += 4
        else:  # L <= l_i
            if r_i <= R:  # r_i <= R
                # [l_i,r_i+1) 削除
                self.count_tiles -= r_i + 1 - l_i  # type: ignore
                self.count_sets -= 1
                self.data.remove(l_i)
                self.data.remove(r_i + 1)
            else:  # R < r_i
                self.count_tiles -= R + 1 - l_i
                self.data.remove(l_i)  # [l_i,r_i+1) 削除
                self.data.add(R + 1)  # [R+1,r_i+1) 挿入
                left += 2

        return left

    def get_count_tiles(self):
        return self.count_tiles

    def get_count_sets(self):
        return self.count_sets

    def get_data(self, closed=False):
        if closed:
            return [j - 1 if i % 2 == 1 else j for i, j in enumerate(self.data)]
        else:
            return list(self.data)


L, R, N = 0, 0, 0


solver = intervalSet([1, N + 1], count_tiles=N)
solver.update_plas(L, R)
print(solver.get_count_tiles())
