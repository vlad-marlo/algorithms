def read_data(filename: str) -> list[tuple[int, ...]]:
    with open(filename) as file:
        n = int(file.readline())
        return [tuple(map(int, file.readline().strip().split())) for _ in range(n)]


def solution(data: list[tuple[int, ...]]) -> int:
    group_a, group_b, group_c = 0, 0, 0
    min_diff = 10**10
    for grp in data:
        a, b, c = sorted(grp)
        assert c == max(grp)
        group_a += a
        group_b += b
        group_c += c
        if c != b and (c - b) % 2 != 0:
            min_diff = min(min_diff, c - b)
    if group_a % 2 == group_b % 2:
        return group_c - min_diff
    return group_c


if __name__ == '__main__':
    print(solution(read_data('27A.txt')), end=' ')
    print(solution(read_data('27B.txt')))
