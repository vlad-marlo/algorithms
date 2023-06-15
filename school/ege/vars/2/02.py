#  ((¬x ∨ z) ≡ (y ∧ ¬w)) → (z ∧ y)\\
print('x y z w S')
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                res = ((not x or z) == (z and not w)) <= (z and y)
                if not res:
                    print(x, y, z, w, x + y + z + w)
