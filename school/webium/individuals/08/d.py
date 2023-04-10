def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def solution(data: list[int]) -> int:
    ans = 0
    endings = [0 for _ in range(10)]
    sm = 0
    for i in data:
        sm += i
        sm %= 10
        if sm == 5:
            ans += endings[0] or 1
        endings[sm % 10] += 1
        ans += endings[abs(sm % 10 - 5)]
    return ans


print(solution(read_data('27A_4.txt')))
print(solution(read_data('27B_4.txt')))
print(solution([8, 7, 12, 23]))

