def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def solution(data: list[int]) -> int:
    ans = 0
    sm = 0
    divs = [10**10 for _ in range(3)]
    for i in data:
        sm += i
        if sm % 3 == 0:
            ans = max(sm, ans)
        now = divs[sm % 3]
        ans = max(ans, sm - now)
        divs[sm % 3] = min(sm, divs[sm % 3])
    return ans


if __name__ == '__main__':
    print(solution(read_data('27A_1.txt')), solution(read_data('27B_1.txt')))