from itertools import product


print(len(set(i for i in product('12345', repeat=5) if i.count('1') == 3)))
