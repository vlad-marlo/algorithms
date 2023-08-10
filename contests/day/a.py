def read_data() -> list[str]:
    return [input() for _ in range(int(input()))]


def solution(data: list[str]) -> int:
    if len(data) <= 1:
        return 1
    now = data[0]
    count = 1
    for i in data[1:]:
        if i <= now:
            count += 1
        now = i
    return count


if __name__ == '__main__':
    print(solution(read_data()))