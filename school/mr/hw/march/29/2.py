print('x y z w')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                res = not (y <= (x == w)) and (z <= x)
                if res:
                    print(x, y, z, w)
