def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def solution(data: list[int]) -> int:
    ans = 0
    ans_sm = 0
    sums = [[10 ** 10, 0] for _ in range(69)]
    sm = 0
    for index, item in enumerate(data):
        sm += item
        if (key := sm % 69) == 0:
            ans_sm, ans = max((ans_sm, ans), (sm, index + 1), key=lambda x: (x[0], -x[1]))
        else:
            pr_s, pr_i = sums[key]
            print(ans, ans_sm, pr_s, pr_i)
            ans, ans_sm = max((ans, ans_sm), (index - pr_i + 1, sm - pr_s), key=lambda x: (x[1], -x[0]))
            sums[key] = min([ans_sm, index], sums[key], key=lambda x: (x[0], -x[1]))
    return ans


print(solution(read_data('271.txt')))
print(solution(read_data('272.txt')))
