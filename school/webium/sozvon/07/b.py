def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        n, m = map(int, file.readline().split())
        return m, [int(file.readline()) for _ in range(n)]


def solution(length: int, data: list[int]) -> tuple[int, int]:
    data = list(map(lambda x: x // 6 + int(x % 6 != 0), data))
    sm = sum(data[:2*length+1])
    ans = sm
    ans2 = sm
    for i in range(2 * length + 1, len(data)):
        sm += data[i] - data[i - 2 * length - 1]
        if sm > ans:
            ans2 = ans
            ans = sm
    return ans, ans2


if __name__ == '__main__':
    print(solution(*read_data('27_A2.txt')))
    print(solution(*read_data('27_B2.txt')))
