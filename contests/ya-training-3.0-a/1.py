def read_data() -> str:
    with open('input.txt') as file:
        return file.read().strip()


def transpond(data: list[list[str]]) -> list[list[str]]:
    result = [["" for _ in range(len(data))] for _ in range(len(data[0]))]
    for i in range(len(data)):
        for j in range(len(data[0])):
            result[j][i] = data[i][j]
    return result


def solution(string: str) -> list[list[str]]:
    string = string.replace(' ', '').replace('\n', '').replace('\r', '')
    chars = sorted(set(string))
    max_count = max(string.count(c) for c in chars)
    result = [[" " for _ in range(max_count+1)] for _ in range(len(chars))]
    for i, char in enumerate(chars):
        result[i][0] = char
        for char_i in range(string.count(char)):
            result[i][char_i+1] = "#"
    return transpond(result)[::-1]


def pprint(data: list[list[str]]) -> None:
    for line in data:
        print(''.join(line))

pprint(solution(read_data()))
