def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        n, m = map(int, file.readline().strip().split())
        data = [0] * 10_000_000
        for _ in range(n):
            key, val = map(int, file.readline().strip().split())
            data[key] = val
        return m, data


def solution(m: int, data: list[int]) -> int:
    data = list(map(lambda x: x // 30 + int(x % 30 > 0), data))
    sm = sum(data[:m*2+1])
    ans = sm
    for i in range(2*m+1, len(data)):
        sm += data[i] - data[i - 2 * m - 1]
        if data[i] > 0:
            ans = max(sm, ans)
    return ans


if __name__ == '__main__':
    print(solution(*read_data('27_A_7275.txt')), end=' ')
    print(solution(*read_data('27_B_7275.txt')))
