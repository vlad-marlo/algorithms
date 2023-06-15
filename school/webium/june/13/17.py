# F = ¬(w ≡ y) ∧ (z → w) ∧ ¬x
print('x y z w S')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                res = (w != y) and (z <= w) and (not x)
                if res:
                    print(x, y, z,  w, x + y + z + w)

