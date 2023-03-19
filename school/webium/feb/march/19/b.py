for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                res = (w and y) or ((x <= w) == (y <= z))
                if not res:
                    print(x, y, z, w)
