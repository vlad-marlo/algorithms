def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        n, m = map(int, file.readline().split())
        return m, [int(file.readline()) for _ in range(n)]


def solution(length: int, data: list[int]) -> int:
    data = list(map(lambda x: x // 6 + int(x % 6 != 0), data))
    data.extend(data[:length * 2+1])
    sm = sum(data[:length * 2 + 1])
    ans = sm
    for i in range(length * 2 + 1, len(data)):
        sm += data[i] - data[i - length * 2 - 1]
        ans = max(ans, sm)
    return ans


if __name__ == '__main__':
    print(solution(*read_data('27_A2.txt')))
    print(solution(*read_data('27_B2.txt')))
