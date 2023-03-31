def read_data() -> dict[int, list[tuple[int, bool]]]:
    with open('26_4.txt') as f:
        n = int(f.readline())
        _res = {}
        for _ in range(n):
            row: int
            place: int
            row, place, from_n = f.readline().strip().split()
            row, place = map(int, (row, place))
            if _res.get(row) is None:
                _res[row] = []
            _res[row].append((place, from_n == '0'))
        return _res


def solution(data: dict[int, list[tuple[int, bool]]]) -> tuple[int, int]:
    not_n = 0
    max_row = 0
    for row_i, row in data.items():
        row.sort(key=lambda x: x[0])
        if len(list(filter(lambda x: x[1], row))) < 500:
            continue
        for i in range(len(row)-1):
            if abs(row[i][0] - row[i+1][0]) == 101 and not any((row[i][1], row[i+1][1])):
                if row_i > max_row:
                    max_row = row_i
                    not_n = len(list(filter(lambda x: not x[1], row)))
    return max_row, not_n


print(*solution(read_data()))
