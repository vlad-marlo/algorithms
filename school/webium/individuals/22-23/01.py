def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def solution(data: list[int]) -> int:
    k = 67
    divs = [10 ** 10 for _ in range(k)]
    divs[0] = 0
    sm = 0
    ans = 0
    for i in data:
        sm += i
        key = sm % k
        ans = max(sm - divs[key], ans)
        divs[key] = min(divs[key], sm)
    return ans


print(solution(read_data('27A_2945.txt')))
print(solution(read_data('27B_2945.txt')))
