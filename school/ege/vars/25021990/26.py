def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def solution(data: list[int]) -> tuple[int, int]:
    data.sort(reverse=True)
    count = len(data) // 3
    sm_final = sum(data)
    sm_before = sm_final
    for i in range(0, (len(data) // 3) * 3, 3):
        sm_final -= min(data[i:i+3])
    for i in range(count):
        sm_before -= data[i]
    return sm_before, sm_final

print(*solution(read_data("26.txt")))
