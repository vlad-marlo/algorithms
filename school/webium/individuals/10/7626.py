def read_data() -> tuple[int, list[tuple[int, int]]]:
    with open('26_7626.txt') as file:
        k = int(file.readline())
        n = int(file.readline())
        data = [(0, 0) for _ in range(n)]
        for i in range(n):
            a, b = map(int, file.readline().strip().split())
            data[i] = (a, b)
        return k, data


def solution(k: int, data: list) -> tuple:
    data.sort()
    n = [0 for _ in range(k)]
    ans = 0
    index = -1
    for a, b in data:
        for i in range(k):
            if n[i] < a:
                ans += 1
                n[i] = b
                index = i
                break
    return ans, index + 1


print(*solution(*read_data()))
