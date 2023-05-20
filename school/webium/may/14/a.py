def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(x) for x in file.readlines()]


def solution(data: list[int]) -> tuple[int, int]:
    mx = max(list(filter(lambda x: len(str(abs(x))) == 2, data)))
    count = 0
    max_sum = 0
    print(mx)
    for i in range(len(data) - 1):
        a, b = data[i:i + 2]
        if any(len(str(x)) == 3 and x > 0 for x in (a, b)) and (sm := a + b) % mx == 0:
            max_sum = max(sm, max_sum)
            count += 1
    return count, max_sum


print(*solution(read_data('17_a.txt')))
