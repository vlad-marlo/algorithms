def read_data() -> str:
    with open('4.txt') as f:
        return f.read()


def solution(data: str) -> int:
    data = data.replace('ABA', 'AB BA').replace('ACA', 'AC CA')
    replace = {
        'BBB': 'BB BB',
        'BBC': 'BB BC',
        'BCB': 'BC CB',
        'CBB': 'CB BB',
        'CCB': 'CC CB',
        'CCC': 'CC CC',
        'BCC': 'BC CC',
        'CBC': 'CB BC',
    }
    while any(i in data for i in replace.keys()):
        for key, val in replace.items():
            data = data.replace(key, val)
    return len(max(data.strip().split(), key=len))


print(solution(read_data()))
# 12 - ответ на задачу, если
