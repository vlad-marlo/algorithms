def read_data() -> tuple[int, str]:
    return int(input().strip()), input().strip()


def solution(replaces: int, string: str) -> int:
    result = 0
    n = len(string)
    for start, char in enumerate(string):
        end = start
        counter = 0
        replaced = 0
        while end + 1 < n and replaced + int(string[end+1] != char) <= replaces:
            replaces += int(string[end+1] != char)
            counter += 1
        result = max(result, end - start + 1)
    return result


if __name__ == '__main__':
    print(solution(*read_data()))
