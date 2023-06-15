graph = {
    'А': 'БГ',
    'Б': 'ЕВ',
    'В': 'ЗД',
    'Г': 'ВДЖ',
    'Д': 'ЗИЖ',
    'Е': 'КМ',
    'Ж': 'ИЛ',
    'З': 'ЕМИ',
    'И': 'Л',
    'К': 'М',
    'Л': 'М',
}


def solution(start, end) -> int:
    if start[-1] == end:
        return 1
    return sum(solution(start + x, end) for x in graph[start[-1]] if x not in start)


print(solution('А', 'М'))