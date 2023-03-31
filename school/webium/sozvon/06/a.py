def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def solution_a(data: list[int]) -> int:
    ans = 0
    n = len(data)
    for start in range(n - 1):
        for end in range(start, n):
            sm = sum(data[start:end])
            if sm % 100 == 0:
                ans = max(ans, sm)
    return ans


def solution(data: list[int]) -> int:
    ans = 0
    sm = 0
    divs = [100**100 for _ in range(100)]
    for i in data:
        sm += i
        if sm % 100 == 0:
            ans = max(sm, ans)
        now = divs[sm % 100]
        ans = max(ans, sm - now)
        divs[sm % 100] = min(sm, now)
    return ans


if __name__ == '__main__':
    print(solution_a(read_data('27A_2945.txt')),solution(read_data('27A_2945.txt')), solution(read_data('27B_2945.txt')))
