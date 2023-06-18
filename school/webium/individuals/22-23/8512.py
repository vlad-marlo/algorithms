def read_data(filename: str) -> tuple[int, list[list[int]]]:
    with open(filename) as file:
        k = int(file.readline())
        return k, [list(map(int, file.readline().strip().split())) for _ in range(int(file.readline()))]


def solution(k: int, data: list[list[int]]) -> tuple[int, int]:
    count, last = 0, 0
    data.sort(key=lambda x: (x[0], x[1]))
    nums = [0 for _ in range(k)]
    for start, end in data:
        for i in range(k):
            if nums[i] <= start:
                nums[i] = end + 1
                last = i + 1
                count += 1
                break
    return count, last


print(*solution(*read_data('26_8512.txt')))