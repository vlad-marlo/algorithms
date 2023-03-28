def read_data(filename: str) -> list[tuple[int, int]]:
    with open(filename) as file:
        n = int(file.readline())
        ans = []
        for _ in range(n):
            a, b = map(int, file.readline().split())
            ans.append((a, b))
        return ans


def solution(data: list[tuple[int, int]]):
    ans = 0
    diff = 1000000
    for a, b in data:
        ans += max(a, b)
        if abs(a - b) % 8 != 2:
            diff = min(diff, abs(a - b))
    if ans % 8 == 2:
        ans -= diff
        assert ans % 8 != 2
    return ans


print(solution(read_data('f4f92895-47c7-4686-a924-458b938be19e.txt')),
      solution(read_data('a4618ab8-f318-4b6c-862c-f4b898c4acf6.txt')))
