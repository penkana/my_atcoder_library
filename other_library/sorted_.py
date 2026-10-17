from sortedcontainers import SortedSet

s = SortedSet([2, 3, 1, 44, 5, 4])
print(s)
# SortedSet([1, 2, 3, 4, 5, 44])　初期化

s.add(10)
print(s)
# SortedSet([1, 2, 3, 4, 5, 44])　addで追加

s.add(2)
print(s)
# SortedSet([1, 2, 3, 4, 5, 10, 44])　重複した要素は１つになる

print(s[0])
# 1 s[0]で最も小さいものを選択

print(s[-1])
# 44 s[-1]で最も小さいものを選択

s.pop()
print(s)
# SortedSet([1, 2, 3, 4, 5, 10]) 一番大きな要素が削除される

print(s.index(2))
# 1

print(s.bisect_left(5))
# 4 二分探索. C++のlower_bound()相当

print(s.bisect_right(5))
# 5 二分探索. C++のupper_bound()相当

print(list(s.irange(3, 8)))
# [3,4,5] 範囲の値を取り出す

s.remove(4)
print(s)
# SortedSet([1, 2, 3, 5, 10]). 要素を削除する

#############

from sortedcontainers import SortedList

s = SortedList([3, 2, 1, 44, 5, 4])
print(s)
# SortedList([1, 2, 3, 4, 5, 44]) 　初期化

s.add(10)
print(s)
# SortedList([1, 2, 3, 4, 5, 10, 44]) addで追加

s.add(2)
print(s)
# SortedList([1, 2, 2, 3, 4, 5, 10, 44]) 重複した要素もOK

print(s[0])
# 1 s[0]で最も小さいものを選択

print(s[-1])
# 44 s[-1]で最も小さいものを選択

s.pop()
print(s)
# SortedList([1, 2, 2, 3, 4, 5, 10])  一番大きな要素が削除される

print(s.index(2))
# 1

print(s.bisect_left(2))
# 1 二分探索. C++のlower_bound()相当

print(s.bisect_right(2))
# 3 二分探索. C++のupper_bound()相当

print(list(s.irange(3, 8)))
# [3,4,5] 範囲の値を取り出す

s.remove(2)
print(s)
# SortedSet([1, 2, 3, 5, 10]) 要素を削除する
