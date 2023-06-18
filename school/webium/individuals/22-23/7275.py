def read_data(filename: str) -> tuple[int, list[tuple[int, int]]]:
    with open(filename) as file:
        n, m = map(int, file.readline().strip().split())
        res: list[tuple[int, int]] = []
        for _ in range(n):
            key: int
            val: int
            key, val = map(int, file.readline().strip().split())
            res.append((key, (val + 29) // 30))
        return m, res


def solution(m: int, data: list[tuple[int, int]]) -> int:
    count, max_count = 0, 0
    left, right = 0, 0
    for start in range(len(data)):
        while right < len(data) and data[right][0] - data[start][0] <= m:
            count += data[right][1]
            right += 1
        while data[start][0] - data[left][0] > m:
            count -= data[left][1]
            left += 1
        max_count = max(count, max_count)
    return max_count


print(solution(*read_data('27_A_7275.txt')))
print(solution(*read_data('27_B_7275.txt')))
