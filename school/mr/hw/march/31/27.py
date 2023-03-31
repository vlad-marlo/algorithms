def read_data(filename: str) -> list[tuple[int, int, int]]:
    with open(filename) as file:
        n = int(file.readline())
        data: list[tuple[int, int, int]] = []
        for _ in range(n):
            a, b, c = sorted(int(x) for x in file.readline().strip().split())
            data.append((a, b, c))
        return data


def solution(data: list[tuple[int, ...]]) -> int:
    min_diff = 1000**1000
    group_a, group_b, group_c = 0, 0, 0
    for group in data:
        a, b, c = group
        group_a += a
        group_b += b
        group_c += c
        if (c - b) % 2 != 0 and c != b:
            min_diff = min(min_diff, c - b)
        if (c - a) % 2 != 0 and a != c:
            min_diff = min(min_diff, c - a)
    if group_a % 2 == group_b % 2:
        return group_c - abs(min_diff)
    return group_c

print(solution(read_data('27-A.txt')))
print(solution(read_data('27-B.txt')))
