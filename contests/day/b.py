def check(s1, s2) -> bool:
    dict_s1 = {}
    dict_s2 = {}
    for pair in zip(s1, s2):
        if dict_s1.setdefault(pair[0], pair[1]) != pair[1] or dict_s2.setdefault(pair[1], pair[0]) != pair[0]:
            return False
    return True


def solution(data: list[str]):
    for i in range(len(data) // 2):
        s1, s2 = data[i * 2], data[i * 2 + 1]
        print('YES' if check(s1, s2) else 'NO')


def read_data() -> list[str]:
    return [input() for _ in range(2 * int(input()))]


if __name__ == '__main__':
    solution(read_data())
