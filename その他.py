# 辞書　逆引き
d = {}
b = {v: k for k, v in d.items()}

# アルファベット順
ord("A")

# 複数のリストを同時にソート
# zipで一つの変数"zip_lists"にまとめる
# ソートの基準としたいリスト(ここではscores)を一番左においてzip
zip_lists = zip([], [], [])
# 昇順でソート
zip_sort = sorted(zip_lists)
# zipを解除
scores, classes, rects = zip(*zip_sort)

# set　に list　を追加
set_a = set()
set_a |= set(["a", "e"])

# 二重リストに別々のソート
# 正数を降順ソートにしたいなら負数を昇順ソートすればよい
data = []
data = sorted(data, key=lambda x: (x[0], -x[1]))

# 長さNの文字列の連続部分文字列の個数
N = 0
ans = N * (N + 1) // 2
