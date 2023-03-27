print('\tx y z w')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                res = w <= ((x <= z) <= y)
                if not res:
                    print('\t', x, y, z, w)
