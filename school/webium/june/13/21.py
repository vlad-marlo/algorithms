#  F = ((w → y) → (x ≡ y)) ∨ ¬z
print('x y z w S')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                res = ((w <= y) <= (x == y)) or not z
                if not res:
                    print(x, y, z, w, x + y + z + w)
