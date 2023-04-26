def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def solution(data: list[int]) -> int:
    div_2 = 0
    div_13 = 0
    div_26 = 0
    for i in data:
        if i % 26 == 0:
            div_26 += 1
        elif i % 13 == 0:
            div_13 += 1
        elif i % 2 == 0:
            div_2 += 1
    return div_26 * (len(data) - div_26) + div_13 * div_2 + int(div_26 * (div_26 - 1) / 2)


def sol_mega_krutoe(data: list[int]) -> int:
    ans = 0
    for i in range(len(data) - 1):
        for j in range(i+1, len(data)):
            ans += (data[i] * data[j]) % 26 == 0
    return ans


print(solution(read_data('27989_A.txt')))
print(solution(read_data('27989_B.txt')))
print(sol_mega_krutoe(read_data('27989_A.txt')))
# print(sol_mega_krutoe(read_data('27989_B.txt')))
