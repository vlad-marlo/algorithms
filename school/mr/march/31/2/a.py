print('x y w F')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                res = (w <= (y == z)) and (y == (z <= x))
                if 1 <= x + y + z + w <= 3 and z == 0:
                    print(x, y, w, int(res))
