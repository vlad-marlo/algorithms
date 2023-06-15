print('x y z F S')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            res = (y <= x) and (x <= z)
            print(x, y, z, int(res), x + y + z)
