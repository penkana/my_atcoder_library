s = "1234"

print(s.zfill(8))
# 00001234

print(s.rjust(8, "0"))
# 00001234

print(s.center(8, "0"))
# 00123400

print(s.ljust(8, "0"))
# 12340000

print("Zero Padding: {:0>8}".format(s))
# Zero Padding: 00001234

s = "-1234"

print("Zero Padding: {:0>8}".format(s))
# Zero Padding: 000-1234
