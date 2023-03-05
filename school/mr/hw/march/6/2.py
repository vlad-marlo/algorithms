print('x y z w')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                res = ((z <= w) or (y == w)) and ((x or z) == y)
                if res and len(list({x, y, z, w})) != 1:
                    print(x, y, z, w)
