print('x y z w')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                res = ((x <= y) or (z <= w)) and ((z == y) <= (w == x))
                if not res:
                    print(x, y, z, w)
