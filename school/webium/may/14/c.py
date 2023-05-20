def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return list(map(int, file.readlines()))


def solution(data: list[int]) -> tuple[int, int]:
    count, mx = 0, 0
    mx_odd = max(filter(lambda x: all(int(n) % 2 != 0 for n in str(x)), data))
    for i in range(len(data) - 1):
        a, b = data[i:i + 2]
        if any(all(int(n) % 2 == 0 for n in str(x)) for x in (a, b)) and (sm := a + b) > mx_odd:
            mx = max(mx, sm)
            count += 1
    return count, mx


print(*solution(read_data('17_c.txt')))
