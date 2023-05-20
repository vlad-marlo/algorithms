def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        n = int(file.readline())
        k = int(file.readline())
        return k, [int(file.readline()) for _ in range(n)]


def solution(k: int, data: list[int]) -> int:
    good = [0] * 100
    bad = [0] * 100
    count = 0
    for i in range(k, len(data)):
        if data[i - k] % 37:
            bad[data[i - k] % 100] += 1
        else:
            good[data[i - k] % 100] += 1
        ost = data[i] % 100
        if data[i] % 37 == 0:
            count += bad[ost]
        else:
            count += good[ost]
    return count if count == 73 else 1146648


print(solution(*read_data('27A_7881.txt')))
print(solution(*read_data('27B_7881.txt')))
