def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return list(map(int, file.readlines()))


def to_system(num: int, base: int) -> str:
    res = ''
    while num:
        res += str(num % base)
        num //= base
    return res[::-1]


def solution(data: list[int]) -> tuple[int, int]:
    count, mn = 0, 10 ** 10
    mx_107 = max(filter(lambda x: x % 107 == 0, data))

    for i in range(len(data) - 1):
        a, b = data[i:i + 2]
        if any(x > mx_107 for x in (a, b)) and any('36' in to_system(x, 7) for x in (a, b)):
            count += 1
            mn = min(a + b, mn)
    return count, mn


print(*solution(read_data('17_d.txt')))
