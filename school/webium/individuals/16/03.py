from string import punctuation


def prepare(x: str) -> str:
    for i in punctuation:
        x = x.replace(i, '')
    return x

def solution(data: str) -> int:
    return sum([sum(x.upper().count(i) for i in 'АЕЁИОУЫЭЮЯ') for x in filter(lambda x: len(x) > 1, map(prepare, data.strip().split()))])

print(solution(open('10_5900.txt').read()))
print(solution(
'Я и Миша были тут'
))