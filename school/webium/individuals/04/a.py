def read_data() -> list[tuple[int, str]]:
    with open('26_7.txt') as f:
        n = int(f.readline())
        ans = []
        for _ in range(n):
            a, b = f.readline().split()
            ans.append((int(a), b))
        return ans


def solution(data: list[tuple[int, str]]) -> tuple[int, int]:
    max_len = 0
    min_key = 0
    for start in range(len(data)):
        data.sort(key=lambda x: x[0], reverse=True)
        res = [data[start]]
        for i in data[start + 1:]:
            if res[-1][0] - 7 >= i[0] and res[-1][1] != i[1]:
                res.append(i)
        if max_len < len(res):
            max_len = len(res)
            min_key = res[-1][0]
    return max_len, min_key


def sol2(data: list[tuple[int, str]]) -> tuple[int, int]:
    data.sort()
    b = [(0, 0) for _ in data]
    for i in range(len(data)):
        m = 0
        min_box = 10000
        for j in range(i):
            if data[i][0] - data[j][0] >= 7 and data[i][1] != data[j][1]:
                if (now := b[j][0]) > m or (now == m and b[j][1] < min_box):
                    m, min_box = b[j]
        if min_box >= 10000:
            min_box = data[i][0]
        b[i] = (m + 1, min_box)
    return b[-1]


print(*sol2(read_data()))
