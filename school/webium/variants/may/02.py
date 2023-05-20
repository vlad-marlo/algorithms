print('row 0: x y z w')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                sm = x + y + z + w
                if sm == 2 and ((w <= y) == (x and z)):
                    print('row 1:', x, y, z, w)
                if sm != 3:
                    continue
                if not (not x or not y or not z or w):
                    print('row 2:', x, y, z, w)
                if (z or w) and y and x:
                    print('row 3:', x, y, z, w)

