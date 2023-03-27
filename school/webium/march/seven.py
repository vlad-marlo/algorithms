from itertools import permutations


def algo(s: str) -> str:
    while '01' in s or '02' in s or '03' in s:
        s = s.replace('01', '1210', 1).replace('02', '10', 1).replace('03', '210', 1)
    return s


print(set(list([algo('0' + ''.join(i)).count('2')] for i in set(permutations(2 * '1' + 5 * '2' + 7 * '3')))))