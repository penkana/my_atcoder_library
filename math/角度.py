import math

# 座標(X,Y)の原点からの角度
X, Y = (0, 0)
angle = math.degrees(math.atan2(X, Y))
if angle < 0:
    angle += 360.0
