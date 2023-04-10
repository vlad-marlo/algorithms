def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def transform(data: list[int]) -> list[int]:
    result = [data[0]]
    now = data[0]
    for i in data[1:]:
        now = min(i if i % 2 else 10**10, now)
        result.append(now)
    return result


def solution(data: list[int]) -> int:
    ans = 100**100
    forwards = transform(data)
    backwards = transform(data[::-1])[::-1]
    for i in range(7, len(data)):
        ans = min(ans, forwards[i-6] * backwards[i])
    return ans if ans != 100**100 else -1


print(solution(read_data('27A.txt')), end=' ')
print(solution(read_data('27B.txt')))
