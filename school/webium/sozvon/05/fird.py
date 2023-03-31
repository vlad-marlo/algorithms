from itertools import permutations


def read_data(filename) -> list[tuple[int, int, int]]:
    with open(filename) as f:
        n = int(f.readline())
        return [tuple(*[map(int, f.readline().split())][:3]) for _ in range(n)]


def solution(data: list[tuple[int, int, int]]) -> int:
    answer = permutations(data[0])
    for triple in data[1:]:
        sums = [sorted([a[0] + b[0], a[1] + b[1], a[2] + b[2]]) for a in answer for b in permutations(triple)]
        groups = [[0 for _ in range(3)] for _ in range(3)]
        for s in sums:
            i = s[0] % 2 + s[1] % 2
            if s[2] > groups[i][2]:
                groups[i] = s
        answer = [x for x in groups if x[2] != 0]
    return answer[1][2]


def sol(data: list[tuple[int, int, int]]) -> int:
    group_a, group_b, group_c = 0, 0, 0
    min_diff = 10000000
    for triple in data:
        a, b, c = sorted(triple)
        group_a += a
        group_b += b
        group_c += c
        if c - b % 2 != 0 and c != b:
            min_diff = min(min_diff, c - b)
    if group_a % 2 == group_b % 2:
        return group_c - min_diff
    return group_c


print(solution(read_data('27-A.txt')), solution(read_data('27-B.txt')))
print(sol(read_data('27-A.txt')), sol(read_data('27-B.txt')))
