data: dict[int, list[int]] = {}
with open('3.txt') as file:
    for _ in range(int(file.readline())):
        key, val = map(int, file.readline().split())
        if data.get(key) is None:
            data[key] = []
        data[key].append(val)
for i in data:
    data[i].sort()

max_row, min_place = 0, 0
for row_i, row in data.items():
    if len(row) < 2:
        continue
    for i in range(len(row) - 1):
        a, b = row[i:i + 2]
        if abs(a - b) == 3:
            if max_row < row_i:
                max_row = row_i
                min_place = a + 1
print(max_row, min_place)  # 8631 7311
