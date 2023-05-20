def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        return int(file.readline()), [int(file.readline()) for _ in range(int(file.readline()))]


def solution(k: int, data: list[int]) -> int:
    _ = [10**10 for _ in range(k)]
    return -1
