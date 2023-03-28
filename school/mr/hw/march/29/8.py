from itertools import product

for i, v in enumerate(product(sorted('ЦАПЛЯ'), repeat=5), start=1):
    if v.count('А') <= 1 and v.count('Ц') == 2 and 'Л' not in v:
        print(i, "".join(v))
        break

