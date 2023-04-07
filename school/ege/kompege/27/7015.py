def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        n = int(file.readline())
        return [int(file.readline()) for _ in range(n)]


def solution(data: list[int]) -> int:
    c = 2
    ans = 0
    for i in range(len(data) - 2):
        if (data[i] > data[i + 1]) != (data[i+1] > data[i+2]):
            c += 1
            ans = max(ans, c)
        else:
            c = 2
    return ans


print(solution(read_data('27_A_7015.txt')))
print(solution(read_data('27_B_7015.txt')))
