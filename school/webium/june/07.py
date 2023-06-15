graph = {
    'a': 'c',
    'c': 'b',
    'b': 'l',
    'd': 'acf',
    'e': 'bdfi',
    'f': 'g',
    'g': 'eh',
    'h': 'ei',
    'i': 'kl',
    'k': 'lb',
    'l': 'e',
}


def solution(start: str, end: str) -> int:
    if start[-1] == end and len(start) > 1:
        return 1
    return sum(solution(start + x, end) for x in graph[start[-1]] if x not in start[1:])


print(solution('e', 'e'))
