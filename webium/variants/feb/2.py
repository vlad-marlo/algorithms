print('x y z F')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            _res = (x == y) or ((y or z) <= x)
            if not _res:
                print(x, y, z, int(_res))
