from collections import deque

# キュー
q = deque()
q.append(1)
v = q.popleft()
q.rotate(1)
# その他の操作はlistと同じ


# スタック
s = deque([])
s.append(1)
s.pop()
s.rotate(1)

# 優先度つきキュー
import heapq

a = []
heapq.heapify(a)
heapq.heappop(a)
heapq.heappush(a, 0)
