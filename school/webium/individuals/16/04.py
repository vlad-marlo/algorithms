from string import punctuation


def prepare(x: str) -> str:
    for i in punctuation:
        x = x.replace(i, '')
    return x


def solution(data: str) -> int:
    c = 0
    for i in data.strip().split():
        c += prepare(i).lower() in ('как', 'что')
    return c


print(solution(open('10_6761.txt').read()))
