graph = {
    'A': 'BCE',
    'B': 'CD',
    'C': 'E',
    'D': 'CF',
    'E': 'DGH',
    'F': 'E',
    'G': 'F',
    'H': 'IGF',
    'I': 'AGE',
}


def solution(start, end) -> int:
    if start[-1] == end and len(start) != 1:
        return 1
    return sum(solution(start + x, end) for x in graph[start[-1]] if x not in start[1:])


print(solution('E', 'E'))