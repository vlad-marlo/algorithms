# ¬(y → w) ∨ (x → z) ∨ ¬x

print('x y z w S')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                res = not (y <= w) or (x <= z) or not x
                if not res:
                    print(x, y, z, w, x + y + z + w)
