def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        n = int(file.readline())
        return [int(file.readline()) for _ in range(n)]


def solution(data: list[int]) -> int:
    mx = 0
    n = len(data)
    s = sum(data)
    sm = 0
    b = []
    for i in data:
        sm += i
        b.append(sm)
    for i in range(n):
        sm += i * data[i]

    mx = sm
    for i in range(1, n):
        sm = b[i-1] * 2 - s
        mx = max(mx, sm)
    return mx

print(solution(read_data('27A_5644.txt')), end=' ')
print(solution(read_data('27B_5644.txt')))

