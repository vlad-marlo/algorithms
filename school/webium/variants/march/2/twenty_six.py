def solution(_data: list[int]) -> tuple[int, int]:
    mn = 0
    sm = 0
    new_data = [_data[0]]
    for i in range(1, len(_data) - 1):
        _, b, _ = sorted(_data[i-1:i+2])
        if _data[i] < b:
            mn += 1
        else:
            sm += _data[i] - b
        new_data.append(b)
    new_data.append(_data[-1])
    return mn, sm


with open('26.txt') as f:
    print(solution([10, 12, 8, 6, 20, 12, 16, 10]))
    data = [int(f.readline()) for _ in range(int(f.readline()))]
    print(*solution(data))
