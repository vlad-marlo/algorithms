import string


def read_data() -> str:
    with open('6.txt') as f:
        return f.read().strip()


def solution(data: str) -> int:
    bad = [f"{'DANOV'[:i]}{l}{'DANOV'[i + 1:]}" for i in range(len('DANOV')) for l in string.ascii_uppercase if
           l != 'DANOV'[i]]
    for i in bad:
        data = data.replace(i, f'{i[:-1]} {i[1:]}')
    return len(max(data.strip().split(), key=len))


print(solution(read_data()))
# ans - 229549
