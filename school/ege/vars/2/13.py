graph = {
    'a': 'bcde',
    'b': 'g',
    'c': 'bghf',
    'd': 'fke',
    'e': 'kl',
    'f': 'hkm',
    'g': 'm',
    'h': 'm',
    'k': 'm',
    'l': 'm',
}


res = set()

def solution(now, want: str) -> int:
    if now[-1] == want:
        res.add(now)
        return 1
    return sum(solution(now + x, want) for x in graph[now[-1]] if x not in now)


print(solution('a', 'm'), len(res))