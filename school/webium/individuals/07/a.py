def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def solution(data: list[int]) -> int:
    ans = 10000000000000000000000000000
    sm = 0
    length = 0
    divs = [(0, 0) for _ in range(777)]
    for i in range(len(data)):
        sm += data[i]
        length += 1
        if sm % 777 == 0 and length > 50:
            ans = min(sm, ans)
        last_i, now = divs[sm % 777]
        if i - last_i >= 50:
            ans = min(sm - now, ans)
        if sm > now:
            divs[sm % 777] = (i, sm)
    return ans


if __name__ == '__main__':
    print(solution(read_data('27A_1.txt')), solution(read_data('27B_2.txt')))