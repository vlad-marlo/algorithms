graph = {
    'A': 'C',
    'B': 'L',
    'C': 'B',
    'D': 'ACF',
    'E': 'IBDF',
    'F': 'G',
    'G': 'EH',
    'H': 'IE',
    'I': 'KL',
    'K': 'BL',
    'L': 'E',
}


def solution(start: str) -> int:
    if start[-1] == start[0] and len(start) != 1:
        return 1
    return sum(solution(start + x) for x in graph[start[-1]] if x not in start[1:])


print(solution('E'))