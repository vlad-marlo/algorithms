def read_data(file: str) -> list[int]:
    with open(file) as f:
        return [int(f.readline()) for _ in range(int(f.readline()))]


def solution(data: list[int]) -> int:
    idx = [-1, *(i for i in range(len(data)) if int((n := data[i]) ** 0.5) ** 2 == n and n != 1), len(data)]
    return max([idx[i + 1] - idx[i] - 1 for i in range(len(idx) - 1)])


print(solution(read_data('27_a.txt')))
print(solution([1, 4, 14, 5, 9, 1, 2, 3, 8, 9]))
print(solution(read_data('27_b.txt')))