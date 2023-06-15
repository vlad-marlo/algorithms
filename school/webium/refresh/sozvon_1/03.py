graph = {
    'А': 'В',
    'Б': 'АГ',
    'В': 'ЕГ',
    'Г': 'ЕД',
    'Д': 'БЗЖ',
    'Е': 'Ж',
    'Ж': 'ИГ',
    'З': 'КЖ',
    'И': 'Г',
    'К': 'ИЖ',
}

res = set()


def solution(start: str) -> int:
    if start[-1] == start[0] and len(start) != 1:
        res.add(start)
        return 1
    return sum(solution(start + x) for x in graph[start[-1]] if x not in start[1:])


solution('Г')
print(max(res, key=len), len(max(res, key=len))-1)
