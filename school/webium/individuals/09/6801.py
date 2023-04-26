def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        n, k = map(int, file.readline().strip().split())
        return k, [int(file.readline()) for _ in range(n)]


def solution(k: int, data: list[int]) -> int:
    sums = [0]
    for i in data:
        sums.append(sums[-1] + i)
    prefixes = []
    for i in range(k, len(sums)):
        prefixes.append(sums[i] - sums[i - k])
    ans = 0
    prefixes.extend([0]*1000000)
    divs = [float('-inf') for _ in range(68)]
    for i in range(k, len(data) + 1):
        n1 = prefixes[i]
        must_be = divs[(68 - (n1 % 68)) % 68]
        if must_be != float('-inf') and n1 + must_be > ans:
            ans = n1 + must_be
        div = prefixes[i + 1 - k] % 68
        divs[div] = max(divs[div], prefixes[i + 1 - k])
    return ans


print(solution(2, [68, 67, 9, 60, 811]))
print(solution(*read_data('27_A_6801.txt')))
print(solution(*read_data('27_B_6801.txt')))
