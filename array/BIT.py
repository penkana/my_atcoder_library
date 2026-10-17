class BIT:
    def __init__(self, n):
        self.size = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l - 1)


bit = BIT(10)

for i in range(10):
    bit.add(i + 1, i + 1)

print(bit.bit)

# val = 1,2,3,4,5,6,7,8,9,10
# sum = 1,3,6,10,15,21,28,36,45,55
for i in range(1, 11):
    print(bit.sum(i))

print(bit.sum(4), bit.sum(2))
print(bit.range_sum(2, 4))
