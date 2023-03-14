def read_data(file_name: str) -> list[int]:
    with open(file_name) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def solution(data: list[int]) -> tuple[int, int]:
    max_s = 0, 0
    for i in range(len(data) - 1):
        a = data[i]
        div = a % 17 == 0
        for j in range(i + 1, len(data)):
            b = data[j]
            if (a - b) % 2 == 0 and (div or b % 17 == 0):
                if a + b > sum(max_s):
                    max_s = a, b
    return max_s


if __name__ == '__main__':
    assert solution([34, 12, 51, 51, 52]) == (51, 51)
    print(*solution(read_data("27_A.txt")), *solution(read_data("27_B.txt")))
