graph = {
    'А': 'БГ',
    'Б': 'Е',
    'В': 'А',
    'Г': 'ЕЖ',
    'Д': 'БЕ',
    'Е': 'ВИК',
    'Ж': 'Е',
    'З': 'ДЕ',
    'И': 'М',
    'К': 'ЖНМ',
    'Л': 'З',
    'М': 'ЗЛ',
    'Н': 'М',
}


def solution(start, end) -> int:
    if start[-1] == end and len(start) != 1:
        return 1
    # res = 0
    # for i in graph[start[-1]]
    return sum(solution(start + x, end) for x in graph[start[-1]] if x not in start[1:])


print(solution('Е', 'Е'))
