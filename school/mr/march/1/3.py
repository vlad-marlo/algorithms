def read_data() -> list[int]:
    with open('3.txt') as f:
        return list(map(int, f.readlines()))


def solution(data: list[int]) -> tuple[int, int]:
    __count = 0
    __max = 0
    nines = list(filter(lambda x: abs(x) % 10 == 9, data))
    avg = sum(nines) / len(nines)
    for i in range(len(data) - 2):
        if all('9' in str(x) for x in data[i:i + 3]) and any(x < avg for x in data[i:i + 3]):
            __max = max(sum(data[i:i + 3]), __max)
            __count += 1
    return __count, __max


if __name__ == '__main__':
    print(*solution(read_data()))
