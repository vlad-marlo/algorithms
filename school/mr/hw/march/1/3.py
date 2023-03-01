def get_data() -> list[int]:
    with open('3.txt') as file:
        return list(map(int, file.readlines()))


def get_all_minimals(data: list[int]) -> int:
    return min([min(abs(data[i]), abs(data[i + 1])) for i in range(len(data) - 1) if 3 in (abs(data[i]) % 10, abs(data[i]) % 10)]) ** 2


def solution(data: list[int]) -> tuple[int, int]:
    __count = 0
    __min = 10 * 100

    magic_num = get_all_minimals(data)

    for i in data:
        if str(i).count('3') == 1 and i >= magic_num:
            __count += 1
            __min = min(__min, i)

    return __count, __min


if __name__ == '__main__':
    print(*solution(get_data()))
    # output:
    # 763 123
