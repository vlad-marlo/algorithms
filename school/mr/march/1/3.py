def read_data() -> list[int]:
    with open('3.txt') as f:
        return list(map(int, f.readlines()))


def solution(data: list[int]) -> tuple[int, int]:
    c = 0
    m = 0
    avg = sum(data) / len(data)
    for i in range(len(data) - 2):
        if all('9' in str(x) for x in data[i:i + 3]) and any(x < avg for x in data[i:i + 3]):
            m = max(sum(data[i:i + 3]), m)
            c += 1
    return c, m


if __name__ == '__main__':
    print(*solution(read_data()))
