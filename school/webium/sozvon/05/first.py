def read_data(filename: str) -> list[tuple[int, int]]:
    with open(filename) as f:
        n = int(f.readline())
        res = []
        for _ in range(n):
            a, b = map(int, f.readline().split())
            res.append((a, b))
        return res


def solution(data: list[tuple[int, int]]) -> int:
    ans = 0
    diff = 10 ** 10
    for a, b in data:
        ans += min(a, b)
        if abs(a - b) % 3 != 0:
            diff = min(diff, abs(a - b))
    if ans % 3 == 0:
        ans += diff
    return ans


if __name__ == '__main__':
    print(solution(read_data('27-A_903.txt')), solution(read_data('27-B_903.txt')))
