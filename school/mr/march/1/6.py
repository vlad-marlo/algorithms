def read_data() -> str:
    with open('6.txt') as f:
        return f.read()


def solution(s: str) -> int:
    replaces = [
        'CAAC', 'CAAD', 'CAAF', 'CAOC', 'CAOD', 'CAOF', 'COOC', 'COOD', 'COOF', 'COAC', 'COAD', 'COAF',
        'DAAC', 'DAAD', 'DAAF', 'DAOC', 'DAOD', 'DAOF', 'DOOC', 'DOOD', 'DOOF', 'DOAC', 'DOAD', 'DOAF',
        'FAAC', 'FAAD', 'FAAF', 'FAOC', 'FAOD', 'FAOF', 'FOOC', 'FOOD', 'FOOF', 'FOAC', 'FOAD', 'FOAF',
    ]
    for rep in replaces:
        s = s.replace(rep, f'{rep[:-1]} {rep[1:]}')
    return len(max(s.split(), key=len))


if __name__ == '__main__':
    print(solution(read_data()))
