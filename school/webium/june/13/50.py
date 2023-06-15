#  (x ≡ y ) ∨ ((y ∨ z) → x)
print('x y z S')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            res = (x == y) or ((y or z) <= x)
            if not res:
                print(x, y, z, x + y + z)
