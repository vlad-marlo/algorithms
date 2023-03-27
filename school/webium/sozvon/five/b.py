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
    pair = data[0]
    mx = 0
    for p in data[1:]:
        sums = [a + b for a in p for b in pair]
        groups = [0, 0, 0]
        for s in sums:
            groups[s % 3] = max(s, groups[s % 3])
        pair = [i for i in groups if i != 0]
        mx = max(mx, max(pair))
    for i in sorted(pair, reverse=True):
        if i % 3 != 0:
            return i
    return ans


if __name__ == '__main__':
    print(solution(read_data('27-A_23.txt')), solution(read_data('27-B_23.txt')))