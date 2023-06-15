graph = {
    'а': 'бжвгд',
    'б': 'ж',
    'в': 'ж',
    'г': 'де',
    'д': 'з',
    'е': 'жз',
    'ж': 'зи',
    'з': 'кил',
    'и': 'км',
    'к': 'лм',
    'л': 'м',
    'м': '',
}


def solution(start: str, end: str) -> int:
    if start[-1] == end:
        return 1
    return sum(solution(start + x, end) for x in graph[start[-1]] if x not in start)


print(solution('а', 'з') * solution('з', 'м'))