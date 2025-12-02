#1 (not)
#2 and /\
#3 or \/
#4 <=
#5 ==
print("x y z w")
for x in 1, 0:
    for y in 1, 0:
        for z in 1, 0:
            for w in 1, 0:
                    the = ((not(y) or z)==((not z) or w)) or (w and y)
                    if the==0: print(x, y, z, w,)
# x y z w
# 1 1 0 0
# 1 0 1 0
# 0 1 1 0
# 0 1 0 0
# 0 0 1 0
