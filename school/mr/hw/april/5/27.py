def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        n = int(file.readline())
        return [int(file.readline()) for _ in range(n)]


def solution(data: list[int]) -> tuple[int, int]:
    divs = [0 for _ in range(160)]
    sevens = [0 for _ in range(160)]
    for i in data:
        ost = i % 160
        divs[ost] = max(divs[ost], i)
        if i % 7 == 0:
            sevens[ost] = max(sevens[ost], i)
    sevens = [i for i in sevens if i != 0]
    divs = [i for i in divs if i != 0]
    mx = 0
    d1, d2 = 0, 0
    for n1 in sevens:
        for n2 in divs:
            if n1 + n2 > mx and n1 % 160 != n2 % 160:
                mx = n1 + n2
                d1, d2 = n1, n2
    return d1, d2


if __name__ == '__main__':
    print(solution([168, 7, 320, 328]))
    print(solution(read_data('28129_A.txt')), end=' ')
    print(solution(read_data('28129_B.txt')))
