def read_data(filename: str) -> tuple[int, dict[int, int]]:
    with open(filename) as file:
        n, m = map(int, file.readline().split())
        print(m, n)
        data = {}
        for _ in range(n):
            km, need = map(int, file.readline().strip().split())
            if data.get(km) is None:
                data[km] = 0
            data[km] += need
        return m, data


def solution(limit: int, homes: dict[int, int]) -> int:
    data = [0 for _ in range(max(homes.keys())+1)]
    for k, v in homes.items():
        data[k] = v // 9 + int(v % 9 != 0)
    sm = sum(data[:2 * limit + 1])
    ans = sm
    for i in range(2 * limit + 1, len(data)):
        sm += data[i] - data[i - 2 * limit - 1]
        ans = max(ans, sm)
    return ans


if __name__ == '__main__':
    print(solution(*read_data('27A_3.txt')))
    print(solution(*read_data('27_B3.txt')))
