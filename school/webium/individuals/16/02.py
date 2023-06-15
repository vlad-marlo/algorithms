def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def solution(data: list[int]) -> int:
    counter = 2
    mx = 2
    for i in range(len(data)-2):
        if (data[i] > data[i+1]) != (data[i+1] > data[i+2]):
            counter += 1
            mx = max(mx, counter)
        else:
            counter = 2
    return mx


print(solution(read_data('27A_2.txt')), end=' ')
print(solution(read_data('27B_2.txt')))
