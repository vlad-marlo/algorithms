def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def solution(data: list[int]) -> int:
    nums = [[] for _ in range(3)]
    for i in data:
        nums[i % 3].append(i)
    for i in range(3):
        nums[i].sort(reverse=True)
    ans = sum(nums[0][:3])
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if (i + j + k) % 3 != 0:
                    continue
                indexes = [i, j,k]
                sm = 0
                for index in set(indexes):
                    sm += sum(nums[index][:indexes.count(index)])
                ans = max(ans, sm)
    return ans


print(solution(read_data('27A_5.txt')))
print(solution(read_data('27B_5.txt')))

