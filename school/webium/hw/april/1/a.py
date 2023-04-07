def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        n = int(file.readline())
        return [int(file.readline()) for _ in range(n)]


def solution(data: list[int]) -> int:
    ans = 0
    sm = 0
    k = 43
    divs = [100**100 for _ in range(k)]
    for i in data:
        sm += i
        if sm % k == 0:
            ans = max(ans, sm)
        now = divs[sm % k]
        ans = max(ans, sm - now)
        divs[sm % k] = min(now, sm)
    return ans


if __name__ == '__main__':
    print(solution(read_data("27A_a.txt")), end=' ')
    print(solution(read_data("27B_a.txt")))
