def read_data() -> list[int]:
    with open('2.txt') as f:
        return list(map(int, f.readlines()))


def solution(data: list[int]) -> tuple[int, int]:
    m, __count = 0, 0
    # max num ending on 12

    for i in range(len(data) - 1):
        if len(list(filter(lambda x: abs(x) % 100 == 12, data[i:i + 2]))) == 1 and sum(
                map(lambda x: x ** 2, data[i:i + 2])) < max(list(filter(lambda x: abs(x) % 100 == 12, data))) ** 2:
            __count += 1
            m = max(m, sum(map(lambda x: x ** 2, data[i:i + 2])))
    return __count, m


if __name__ == '__main__':
    print(*solution(read_data()))
