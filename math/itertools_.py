import math
import itertools

l = []
n = 1
k = 1


# 階乗
print(math.factorial(n))
# 順列
print(math.perm(n, k))
print(list(itertools.permutations(l, k)))
# 組み合わせ
print(math.comb(n, k))
print(list(itertools.combinations(l, k)))
# 重複あり組み合わせ
print(math.comb(n + k - 1, k))
print(itertools.combinations_with_replacement(l, k))
# ランレングス圧縮
print([(k, len(list(g))) for k, g in itertools.groupby(l)])


# RUN LENGTH ENCODING str -> str
# example) "aabbbbaaca" -> "a2b4a2c1a1"
def runLengthEncodeToString(S: str) -> str:
    grouped = itertools.groupby(S)
    res = ""
    for k, v in grouped:
        res += k + str(len(list(v)))
    return res
