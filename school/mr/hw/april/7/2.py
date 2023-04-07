print('x y z w S')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                res = ((x <= (y and w)) and (not z or x or y)) != w
                if res:
                    print(x, y, z, w, x + y + z + w)
