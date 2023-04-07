def read_data(filename: str) -> tuple[int, int, dict[int]]:
    with open(filename) as file:
        n, v, m = map(int, file.readline().split())
        data = {}
        for _ in range(n):
            key, val = map(int, file.readline().strip().split())
            data[key] = val
        return v, m, data


def sol(v: int, m: int, d: dict[int]) -> int:
    data = [0 for _ in range(max(d.keys())+1)]
    for key, val in d.items():
        data[key] = val // v + int(val % v != 0)
    sm = sum(data[:m*2+1])
    ans = sm
    for i in range(m * 2 + 1, len(data)):
        sm += data[i] - data[i - 2 * m - 1]
        ans = max(ans, sm)
    return ans


def solution(v: int, m: int, data_in: dict[int]) -> int:
    data = [0 for _ in range(max(data_in.keys()) + 1)]
    for key, val in data_in.items():
        data[key] = val // v + int(val % v > 0)
    sm = sum(data[:m * 2 + 1])
    ans = sm
    for i in range(m * 2 + 1, len(data)):
        sm += data[i] - data[i - m * 2 - 1]
        if data[i] != 0:
            ans = max(sm, ans)
    return ans


if __name__ == '__main__':
    print(solution(*read_data('27A_44.txt')), end=' ')
    print(solution(*read_data('27B_44.txt')), end=' ')
    print(solution(*read_data('hw_test.txt')))
    print(sol(*read_data('27A_44.txt')), end=' ')
    print(sol(*read_data('27B_44.txt')), end=' ')
    print(sol(*read_data('hw_test.txt')))
