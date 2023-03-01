def read_data() -> list[int]:
    with open('17.txt') as file:
        return list(map(int, file.readlines()))


def get_answer(data: list[int]) -> tuple[int, int]:
    __count = 0
    __max = 0
    for i in range(len(data) - 1):
        for j in range(i, len(data)):
            a, b = data[i], data[j]
            if a != b and (a + b) % 8 == 0:
                __count += 1
                __max = max(__max, a + b)
    return __count, __max


def get_answer_old(data: list[int]) -> tuple[int, int]:
    __count = 0
    __max = 0
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            a, b = data[i], data[j]
            __count += ((a + b) % 8 == 0)
            __max = max(__max, (a + b) * int((a + b) % 8 == 0))
    return __count, __max


def main():
    c, m = get_answer(list(set(read_data())))
    assert c <= 10_000 * 9_999
    print(c, m)


if __name__ == '__main__':
    main()
