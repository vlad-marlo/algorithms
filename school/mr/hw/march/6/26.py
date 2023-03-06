def read_data() -> list[int]:
    with open('inf_22_10_20_26.txt') as f:
        return [int(f.readline()) for _ in range(int(f.readline()))]


def solution(data: list[int]) -> tuple[int, int]:
    m, s = 0, sum([i for i in data if i <= 100])
    nums = [i for i in data if i > 100]
    nums.sort()
    for i in range(len(nums) // 2+1):
        if i == len(nums) - i - 1:
            s += nums[i]
            continue
        s += nums[i]*0.7
        m = nums[i]
        s += nums[len(nums)-i-1]
    return round(s+0.5), m


assert solution([125, 100, 490, 215, 144, 320]) == (1314, 144)
print(solution(read_data()))
