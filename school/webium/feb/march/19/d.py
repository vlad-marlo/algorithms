from itertools import permutations

print(len([i for i in set(permutations('амфибрахий')) if 'аафии' in ''.join(i) or 'иифаа' in ''.join(i)]))
