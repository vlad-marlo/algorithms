def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def solution(data: list[int]) -> int:
    ans = 0
    divs = [10**10 for _ in range(32)]
    sm = 0
    for i in data:
        sm += i
        if sm % 32 == int('r', 32):
            ans = max(ans, sm)
        now = divs[sm % 32]
        ans = max(ans, sm - now)
        divs[sm % 32] = min(now, sm)
    return ans


print(solution(read_data('27A_2.txt')))
print(solution(read_data('27B_2.txt')))
