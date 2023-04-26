print('x y z w')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                res = not y and (x <= (z != w)) or z
                if not res:
                    print(x, y, z, w, x + y + z + w)
