print('x y z w')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                _res = ((not y or w) == (not x or not z)) and (x or w)
                if _res and not w and sum([x, y, z, w]) <= 2:
                    print(x, y, z, w, 1)
