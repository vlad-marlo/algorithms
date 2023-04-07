def read_data() -> list[int]:
    with open(file='17.txt') as file:
        return [int(x) for x in file.readlines()]


def solution(data: list[int]) -> tuple[int, int]:
    count = 0
    mx = 0
    for i in range(len(data) - 1):
        a = data[i]
        for j in range(i, len(data)):
            b = data[j]
            if i == j:
                continue
            if (a * b) % 10 == 0:
                count += 1
                mx = max(mx, a + b)
    return count, mx


print(*solution(read_data()))
