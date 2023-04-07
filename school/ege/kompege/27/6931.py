def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def solution(data: list[int]) -> int:
    data.extend(data)
    mx = 0
    now = data[0] // 2
    last = data[0]
    for i, item in enumerate(data, start=1):
        mx = max(now, mx)
        if item % 2 != last % 2:
            now = item // 2
        else:
            now += item // 2
        last = item
    return mx


print(solution(read_data('27A_6931.txt')))
print(solution(read_data('27B_6931.txt')))
