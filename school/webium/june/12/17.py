graph = {
    'A': 'BCH',
    'B': 'CD',
    'C': 'E',
    'D': 'CEF',
    'E': 'AI',
    'F': 'E',
    'G': 'F',
    'H': 'EFD',
    'I': 'H',
}


def solution(start: str) -> int:
    if start[-1] == start[0] and len(start) != 1:
        print(start)
        return 1
    return sum(solution(start + x) for x in graph[start[-1]] if x not in start[1:])


print(solution('E'))
