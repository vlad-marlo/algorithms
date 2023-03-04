def read_data(file: str) -> list[int]:
    with open(file) as f:
        return [int(f.readline()) for _ in range(int(f.readline()))]


def solution(data: list[int]) -> int:
    c = 0
    for j in range(1, len(data), 3):
        i = (j - 1) // 3
        assert j == (3 * i) + 1
        if data[i] * 2.5 == data[j] or data[j] * 2.5 == data[i]:
            c += 1
    return c


print(solution([2, 5, 3, 14, 27]))
print(solution(read_data('27_a.txt')))
print(solution(read_data('27_b.txt')))
