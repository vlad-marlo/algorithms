# Решение для файла B (более быстрое)

f = open('27_b.txt')  # открываем файл

n = int(f.readline())
c = [int(i) for i in f]

maxLen = 0
currLen = 0
flag = False
for i in range(n):
    if int(c[i] ** 0.5) ** 2 == c[i] and c[i] > 1:
        if flag:
            maxLen = max(maxLen, currLen)
            currLen = 0
        flag = not flag
    else:
        if flag:
            currLen += 1
print(maxLen)
