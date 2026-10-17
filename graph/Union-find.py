class DisjointSet:
    def __init__(self) -> None:
        self.parent = {}
        self.size = {}

    def makeSet(self, set):
        for e in set:
            self.parent[e] = e
            self.size[e] = 1

    def Find(self, x):
        if x not in self.parent:
            return None
        elif self.parent[x] == x:
            return x
        else:
            # 経路圧縮
            self.parent[x] = self.Find(self.parent[x])
            return self.parent[x]

    def Union(self, x, y):
        a = self.Find(x)
        b = self.Find(y)

        if a == None or b == None or a == b:
            return False

        # union by sizeで効率化
        if self.size[a] < self.size[b]:
            a, b = b, a

        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

    def issame(self, x, y):
        a = self.Find(x)
        b = self.Find(y)
        if a == b == None:
            return False
        return a == b

    def getsize(self, x):
        return self.size[self.Find(x)]

def printSet(set, ds):
    return [ds.Find(i) for i in set]

def test_unionfind():
    ds = DisjointSet()
    ds.makeSet([1, 2, 3, 4, 5, 6])
    ds.Union(1, 2)
    ds.Union(2, 3)
    ds.Union(5, 6)

    assert ds.issame(1, 3) == True
    assert ds.issame(2, 5) == False

    ds.Union(1, 6)

    assert ds.issame(2, 5) == True