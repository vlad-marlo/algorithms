# (¬z ≡ ¬y) ∨ (¬x ∧ y) ∨ w
print('x y z w S')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                res = (z == y) or ((not x) and y) or w
                if not res:
                    print(x, y, z, w, x + y + z + w)
