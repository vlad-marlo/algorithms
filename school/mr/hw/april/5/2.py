print('x y z w S')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                res = (x <= y) and (y != z) and (z or w)
                if res:
                    print(x, y, z, w, x + y + z + w)
