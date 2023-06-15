graph = {
    'А': 'БВГ',
    'Б': 'Д',
    'В': 'ДЕ',
    'Г': 'ВЕИ',
    'Д': 'ЛК',
    'Е': 'ДЛЖИ',
    'Ж': 'ЛМ',
    'И': 'ЖМН',
    'К': 'МП',
    'Л': 'КМ',
    'М': 'ПСРН',
    'Н': 'Р',
    'П': 'С',
    'Р': 'С',
    'С': '',
}

unique_paths = set()


def solution(now, want):
    if now[-1] == want:
        if len(now) == 1:
            return
        unique_paths.add(now)
        return
    for i in graph[now[-1]]:
        solution(now + i, want)


for i in graph.keys():
    solution(i, 'С')
print(len(unique_paths))
