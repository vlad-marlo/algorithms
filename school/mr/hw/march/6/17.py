def read_data() -> list[int]:
    with open('17.txt') as f:
        return list(map(int, f.readlines()))


def solution(data: list[int]) -> tuple[int, int]:
    m, c = 0, 0
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            a, b = data[j], data[i]
            if (a * b) % 7 == 0 and a % 160 != b % 160:
                c += 1
                m = max(m, a + b)
    return c, m


assert solution([168, 7, 320, 328]) == (4, 488)
print(solution(read_data()))

