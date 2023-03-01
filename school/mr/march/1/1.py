def read_data() -> list[int]:
    with open('1.txt') as f:
        return list(map(int, f.readlines()))


def solution(data: list[int]) -> tuple[int, int]:
    __min, __count = 10 ** 10, 0
    min_9 = max(filter(lambda x: abs(x) % 10 == 9, data))
    for i in range(len(data) - 1):
        a, b = data[i:i+2]
        if len(list(filter(lambda x: abs(x) % 10 == 9, data[i:i+2]))) == 1 and a ** 2 + b ** 2 < min_9 ** 2:
            __count += 1
            __min = min(__min, a ** 2 + b ** 2)
    return __count, __min


if __name__ == '__main__':
    print(*solution(read_data()))