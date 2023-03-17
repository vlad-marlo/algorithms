def read_data() -> list[int]:
    with open('26_3.txt') as f:
        return [int(f.readline()) for _ in range(int(f.readline()))]


def solution(data: list[int], offset: int) -> tuple[int, int]:
    data.sort(reverse=True)
    ans = [data[0]]
    for i in data[1:]:
        if abs(ans[-1] - i) >= offset:
            ans.append(i)
    return ans[-1], len(ans)


print(solution([43, 40, 32, 40, 30], 3))
print(solution(read_data(), 3))
