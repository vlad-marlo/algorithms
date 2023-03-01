def read_data() -> list[int]:
    with open('1.txt') as file:
        return list(map(int, file.readlines()))


def get_square_of_max_with_9_at_the_end(data: list[int]) -> int:
    return max(filter(lambda x: str(x)[-1] == '9', data)) ** 2


def solution(data: list[int]) -> tuple[int, ...]:
    __count = 0
    __min = 100 ** 100

    sq = get_square_of_max_with_9_at_the_end(data)

    for i in range(len(data) - 1):
        a, b = data[i], data[i + 1]
        __sum = a ** 2 + b ** 2
        if len([i for i in (a, b) if str(i)[-1] == '9']) == 1 and __sum < sq:
            __count += 1
            __min = min(__min, __sum)

    return __count, __min


def main():
    # ответ - 1428 356530
    print(*solution(read_data()))


if __name__ == '__main__':
    main()
