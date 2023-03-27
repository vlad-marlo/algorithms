def read_data(file: str) -> list[tuple[int, int, int]]:
    with open(file) as f:
        n = int(f.readline())
        res = []
        for _ in range(n):
            a, b, c = sorted(map(int, f.readline().split()))
            res.append((a, b, c))
        return res


def soluton(data: list[tuple[int, int, int]]) -> int:
    ans = 0
    dif = 100**100
    for triple in data:
        ans += triple[2]
        assert triple[2] == max(triple)
        if (now_diff := triple[2] - triple[1]) % 91 != 0:
            dif = min(dif, now_diff)
        elif (now_diff := triple[2] - triple[0]) % 91 != 0:
            dif = min(dif, now_diff)
    if ans % 91 == 0:
        print(f'{dif=}')
        return ans - dif
    return ans


if __name__ == '__main__':
    print(soluton(read_data('27_A_6057.txt')), end=" ")
    print(soluton(read_data('27_B_6057.txt')))
