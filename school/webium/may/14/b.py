def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return list(map(int, file.readlines()))


def solution(data: list[int]) -> tuple[int, int]:
    max_ending_on_54 = max(filter(lambda x: abs(x) % 100 == 54, data))
    count = 0
    mx = 0
    for i in range(len(data) - 1):
        a, b = data[i:i + 2]
        if (abs(a) + abs(b)) <= max_ending_on_54 and abs(a) % 10 == abs(b) % 10:
            count += 1
            mx = max(mx, a, b)
    return count, mx


print(*solution(read_data('17_b.txt')))
