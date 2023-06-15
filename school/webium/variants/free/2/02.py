# ((y ˅ z) → x) ˅ (x ≡ z)

print('x y z')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            res = ((y or z) <= x) or (x == z)
            if not res:
                print(x, y, z, x + z + y)