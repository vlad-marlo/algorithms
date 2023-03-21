data = [[0 for _ in range(10001)] for _ in range(10001)]
with open('1.txt') as file:
    for _ in range(int(file.readline())):
        row, col = map(int, file.readline().split())
        data[row][col] += 1

min_row = 0
max_count = 0
for row_i in range(len(data)):
    row = data[row_i]
    local = 0
    for i in row:
        if i:
            local += 1
            if local > max_count:
                max_count = local
                min_row = row_i
        else:
            local = 0

# 10 2786
print(max_count, min_row)
