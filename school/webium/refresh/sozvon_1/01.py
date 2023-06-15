graph = {
    'А': 'БГ',
    'Б': 'Д',
    'В': 'АГД',
    'Г': 'ЖЕ',
    'Д': 'ЕИЛ',
    'Е': 'ВЛ',
    'Ж': 'Е',
    'И': 'Л',
    'К': 'Ж',
    'Л': 'ЖК',
}


def solution(start: str) -> int:
    if start[-1] == start[0] and len(start) != 1:
        return 1
    return sum(solution(start + x) for x in graph[start[-1]] if x not in start[1:])


print(solution('В'))
