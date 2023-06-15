def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def solution(data: list[int]) -> int:
    mx = 0
    count_of_odd, count_of_even = 0, 0
    endings = {}
    for i in data:
        if i % 2:
            count_of_odd += 1
        else:
            count_of_even += 1
        if count_of_odd == count_of_even:
            mx = max(mx, 2 * count_of_odd)
        if (key := abs(count_of_even - count_of_odd)) in endings:
            mx = max(mx, count_of_odd + count_of_even - endings[key])
        else:
            endings[key] = count_of_odd + count_of_even
    return mx


print(solution(read_data('27A_1.txt')), end=' ')
print(solution(read_data('27B_1.txt')))
