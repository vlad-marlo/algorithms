graph = {
    'А': 'БВГД',
    'Б': 'ВЕЖ',
    'В': 'Ж',
    'Г': 'ВЖ',
    'Д': 'ГЖИЗ',
    'Е': 'ЖИ',
    'Ж': 'И',
    'З': 'И',
    'И': 'КЛМ',
    'К': 'М',
    'Л': 'М',
    'М': '',
}


def solution(start, end, want, exclude) -> int:
    if start[-1] == end:
        print(start, 1 if want in start else 0)
        return 1 if want in start else 0
    assert exclude not in start, f'{exclude} in {start}'
    return sum(solution(start + x, end, want, exclude) for x in graph[start[-1]] if x not in start and x not in exclude)


print(solution('А', 'М', 'В', 'Д'))
