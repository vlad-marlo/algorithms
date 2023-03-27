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


print(solution(read_data('27-A.txt')), solution(read_data('27-B.txt')))
