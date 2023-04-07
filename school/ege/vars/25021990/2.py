print('x y z w S')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                res = (not x or not (not y or  z)) or w
                if not res:
                    print(x, y, z, w, sum((x, y, z, w)))
