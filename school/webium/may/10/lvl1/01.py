def solution(data: list[int]) -> int:
    count = 0
    for i in range(len(data) - 6):
        for j in range(i + 6, len(data)):
            count += (data[j] - data[i]) % 13 == 0 and (data[i] % 2 == 0 or data[j] % 2 == 0)
    return count


def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


print(solution(read_data('27A_1.txt')), end=' ')
print(solution(read_data('27B_1.txt')))
