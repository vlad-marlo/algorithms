data: dict[int, list[int]] = {}
with open('2.txt') as file:
    for _ in range(int(file.readline())):
        row, col = map(int, file.readline().split())
        if data.get(row) is None:
            data[row] = []
        data[row].append(col)
for row in data:
    data.get(row, []).sort()
max_col = 0
min_place = 0
for key, val in data.items():
    if len(val) < 2:
        continue
    for i in range(len(val) - 1):
        a, b = val[i:i + 2]
        if b - a - 1 == 13:
            if max_col < key:
                max_col = key
                min_place = a+1

# 50449 59966
print(min_place, max_col)
