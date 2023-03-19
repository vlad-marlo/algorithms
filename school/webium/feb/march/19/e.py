def read_data() -> list[int]:
    with open('17_6605.txt') as file:
        return [int(x) for x in file]


def solution(data: list[int]) -> tuple[int, int]:
    count = 0
    max_diff = 0
    max_five = 0
    for i in data:
        if abs(i) % 10 == 5:
            max_five = max(i, max_five)
    for i in range(len(data) - 1):
        a, b = data[i], data[i + 1]
        if ((abs(a) % 10 == 5 and (abs(b) % 10 != 5)) or (abs(b) % 10 == 5 and (abs(a) % 10 != 5))) \
                and (abs(a ** 2 - b ** 2) <= max_five ** 2):
            count += 1
            max_diff = max(abs(a ** 2 - b ** 2), max_diff)
    return count, max_diff


print(*solution(read_data()))
