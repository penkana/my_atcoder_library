from collections import defaultdict


d = defaultdict(int)  # list,set...
d = defaultdict(lambda: 1)


def init_dict():
    return 10


d = defaultdict(init_dict)

print(d.get("a"))
# Noneが返る
print(d)
d = dict(d)
print(type(d))
