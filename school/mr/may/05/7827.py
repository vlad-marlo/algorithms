def read_data(filename: str) -> tuple[int, list[int]]:
    with open(filename) as file:
        return int(file.readline()), [int(file.readline()) for _ in range(int(file.readline()))]


def get_maxes(data: list[int], even: bool) -> list[int]:
    res = []
    if (data[0] % 2 == 0) == even:
        res.append(data[0])
    else:
        res.append(0)
    for i in data[1:]:
        res.append(max(res[-1], i if (i % 2 == 0) == even else 0))
    return res


def solution(k: int, data: list[int]) -> int:
    forwards_odd = get_maxes(data, False)
    forwards_even = get_maxes(data, True)
    backwards_odd = get_maxes(data[::-1], False)[::-1]
    backwards_even = get_maxes(data[::-1], True)[::-1]
    mx = 0
    for i in range(len(data)-k):
        mx = max(mx, forwards_odd[i]+backwards_even[i+k])
        mx = max(mx, forwards_even[i]+backwards_odd[i+k])
    return mx


print(solution(*read_data('27A_7827.txt')))
print(solution(*read_data('27B_7827.txt')))
