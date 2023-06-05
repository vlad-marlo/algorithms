print('x y z w S')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                res = (not x or y or z) and (x or not y or not w)
                if not res:
                    print(x, y, z, w, x + z + w + y)
