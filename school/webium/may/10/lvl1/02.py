def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def solution(data: list[int]) -> int:
    counts = [1 if data[0] % 23 == 0 else 0]
    for i in data:
        counts.append(counts[-1] + 1 if i % 23 == 0 else 0)
    return -1
