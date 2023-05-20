def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        return int(file.readline()), [int(file.readline()) for _ in range(int(file.readline()))]


def solution(k: int, data: list[int]) -> int:
    divs = [0] * k
    ans = 0
    sm = 0
    for i in range(1, len(data)):
        sm = (sm + data[i - 1]) % k
        if divs[sm] and ans < divs[sm] + data[i]:
            ans = divs[sm] + data[i]
        divs[sm] = max(divs[sm], data[i - 1])
    return ans


print(solution(*read_data('27A_7856.txt')))
print(solution(*read_data('27B_7856.txt')))
