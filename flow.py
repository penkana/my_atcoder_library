from collections import deque
import sys

sys.setrecursionlimit(10**6)


class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.level = []
        self.it = []

    def add_edge(self, fr, to, cap):
        # [行先, 容量, 逆方向エッジのインデックス]
        self.graph[fr].append([to, cap, len(self.graph[to])])
        self.graph[to].append([fr, 0, len(self.graph[fr]) - 1])

    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        queue = deque([s])
        while queue:
            v = queue.popleft()
            for to, cap, rev in self.graph[v]:
                if cap > 0 and self.level[to] < 0:
                    self.level[to] = self.level[v] + 1
                    queue.append(to)
        # シンクtに到達できればTrue
        return self.level[t] >= 0

    def dfs(self, v, t, f):
        if v == t:
            return f
        # self.it[v] により、前回の探索で調べ終えたエッジをスキップする
        for i in range(self.it[v], len(self.graph[v])):
            self.it[v] = i
            to, cap, rev = self.graph[v][i]
            # レベルが1つ先かつ容量があるエッジのみ進む
            if cap > 0 and self.level[v] < self.level[to]:
                d = self.dfs(to, t, min(f, cap))
                if d > 0:
                    # フローの更新
                    self.graph[v][i][1] -= d
                    self.graph[to][rev][1] += d
                    return d
        return 0

    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            # BFSを行うたびにポインタを初期化
            self.it = [0] * self.n
            while True:
                f = self.dfs(s, t, float("inf"))
                if f == 0:
                    break
                flow += f
        return flow


##################### 二部マッチング
# インスタンス化 (頂点数: S(1) + 学生N(3) + サークルM(3) + T(1) = 8)
N, M = 3, 3
S, T = 0, N + M + 1
dinic = Dinic(N + M + 2)

# 1. Sから学生(1,2,3)へエッジを貼る。容量は1
for i in range(1, N + 1):
    dinic.add_edge(S, i, 1)

# 2. サークル(4,5,6)からTへエッジを貼る。容量は1
for j in range(N + 1, N + M + 1):
    dinic.add_edge(j, T, 1)

# 3. 希望関係のエッジ (学生1はサークル4と5、学生2はサークル4...)。容量は1
dinic.add_edge(1, 4, 1)
dinic.add_edge(1, 5, 1)
dinic.add_edge(2, 4, 1)
dinic.add_edge(3, 6, 1)

# 最大流 = 最大マッチング数 を計算
result = dinic.max_flow(S, T)


##################### 燃やす埋める
# 頂点番号の定義
N = 4
S = 0
T = N + 1
PROJ1, PROJ2 = 1, 2
MACH_A, MACH_B = 3, 4

# Dinicインスタンス作成 (頂点数 6: S, T, Proj*2, Mach*2)
dinic = Dinic(T + 1)
total_profit = 0

# 1. 利益を S 側につなぐ
# プロジェクト1: 利益100
dinic.add_edge(S, PROJ1, 100)
total_profit += 100
# プロジェクト2: 利益150
dinic.add_edge(S, PROJ2, 150)
total_profit += 150

# 2. コストを T 側につなぐ
# 機材A: コスト80
dinic.add_edge(MACH_A, T, 80)
# 機材B: コスト120
dinic.add_edge(MACH_B, T, 120)

# 3. 依存関係（制約）を容量無限大でつなぐ
# プロジェクト1 をやるなら 機材A が必須
dinic.add_edge(PROJ1, MACH_A, float("inf"))
# プロジェクト2 をやるなら 機材A と 機材B が必須
dinic.add_edge(PROJ2, MACH_A, float("inf"))
dinic.add_edge(PROJ2, MACH_B, float("inf"))

# 4. 最大流（最小カット）を計算
min_loss = dinic.max_flow(S, T)

# 5. 最大利益の算出
max_profit = total_profit - min_loss
