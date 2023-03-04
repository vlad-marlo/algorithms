def read_data() -> list[tuple[int, int, int, int, int, int, int, int]]:
    with open('9.csv') as file:
        data = file.readlines()
        res = []
        for line in data:
            a, b, c, d, e, f, g, h = map(int, line.strip().split(','))
            res.append((a, b, c, d, e, f, g, h))
        return res


def solution(data: list[tuple[int, int, int, int, int, int, int, int]]) -> int:
    c = 0
    for line in data:
        if line.count(0) != 1:
            continue
        idx = line.index(0) % 4
        indexes = [*range(4)]
        indexes.remove(idx)
        print(*((line[x1], line[x2]) for x1 in indexes for x2 in [i for i in indexes if i != x1]))
        for x1 in indexes:
            loc = indexes[:]
            loc.remove(x1)

            if not any(line[x1] == line[x1] or line[x1 + 4] == line[x1 + 4] for x1 in loc):
                break
        else:
            c += 1
    return c


if __name__ == '__main__':
    print(solution(read_data()))