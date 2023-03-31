def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [1 if int(file.readline()) % 2 else -1 for _ in range(int(file.readline()))]


def solution(data: list[int]) -> int:
    ans = 0
    for start in range(len(data) - 1):
        for end in range(start, len(data)):
            c = 0
            sm = 0
            for i in data[start:end]:
                c += i
                sm += 1
            if c == 0:
                ans = max(ans, sm)
    return ans


if __name__ == '__main__':
    print(solution(read_data('27A_5986.txt')), end=' ')
    print(solution(read_data('27B_5986.txt')))
