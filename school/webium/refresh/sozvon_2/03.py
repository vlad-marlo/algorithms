def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(x) for x in file.readlines()]


def solution(data: list[int]) -> tuple[int, int]:
    count, mx = 0, 0
    mx_eight = min(filter(lambda x: 100 <= abs(x) <= 999 and abs(x) % 10 == 8, data))
    print(mx_eight)
    for i in range(len(data) - 2):
        a, b, c = sorted(data[i:i + 3], key=lambda x: x ** 2)
        if (a ** 2 <= mx_eight ** 2 < b ** 2) and any(100 <= abs(x) <= 999 for x in (a, b, c)):
            count += 1
            mx = max(mx, a + b + c)
    return count, mx


print(*solution(read_data('03.txt')))
