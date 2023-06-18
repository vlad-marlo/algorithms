def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(x) for x in file.readlines()]


def solution(data: list[int]) -> tuple[int, int]:
    count, mn = 0, 10 ** 10
    min_positive = min([i for i in range(1, max(data)+1) if i in data])

    for i in range(len(data) - 3):
        if all(abs(x) % 111 != min_positive for x in data[i:i+4]):
            count += 1
            mn = min(mn, sum(data[i:i+4]))
    return count, mn


print(solution(read_data('17_1.txt')))
