graph = {
    'А': 'ЖБ',
    'Б': 'ЗВ',
    'В': 'Г',
    'Г': 'ЖЗДЕ',
    'Д': 'Е',
    'Е': 'АЖ',
    'Ж': 'З',
    'З': 'АВ',
}


def solution(start: str) -> int:
    if start[-1] == start[0] and len(start) != 1:
        return 1
    return sum(solution(start + x) for x in graph[start[-1]] if x not in start[1:])


print(solution('З'))
