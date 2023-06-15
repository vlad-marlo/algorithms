# ((x → y) ∧ (z ∨ w)) → ((x ≡ w) ∨ (y ∧ ¬z)).

print('x y z w S')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                res = ((x <= y) and (z or w)) <= ((x == w) or (y and not z))
                if not res:
                    print(x, y, z, w, x + y + z + w)
