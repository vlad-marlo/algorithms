# ¬(z ≡ x) /\ (y /\ x) \/ (¬(w → z) /\ (x → y))


print('x y z w R S')

for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                res = (z != x) and (y and x) or (not(w <= z) and (x <= y))
                print(x, y, z, w, int(res), x + y + z + w)