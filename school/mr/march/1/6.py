def read_data() -> str:
    with open('6.txt') as f:
        return f.read()


def solution(s: str) -> int:
    sog = 'CDF'
    gl = 'AO'
    replaces = [f'{l1}{l2}{l3}{l4}' for l1 in sog for l2 in gl for l3 in gl for l4 in sog]
    while any(rep in s for rep in replaces):
        for rep in replaces:
            s = s.replace(rep, f'{rep[:-1]} {rep[1:]}')
    assert not any(rep in s for rep in replaces)
    return len(max(s.split(), key=len))


if __name__ == '__main__':
    print(solution(read_data()))
