n, m, q = map(int, input().split())
dc = [[1] * m for _ in range(n)]  # изначально все включены
dr = [0] * m  # накапливаем количество перезапусков
for _ in range(q):
    cmd, *a, = input().split()
    *a, = map(int, a)
    if cmd == 'RESET':
        i = a[0]
        dc[i - 1] = [1] * m
        dr[i - 1] += 1
    elif cmd == 'DISABLE':
        i, j = a
        dc[i - 1][j - 1] = 0
    elif cmd == 'GETMAX':
        ans = max(range(n), key=lambda x: (dr[x] * sum(dc[x]), -x)) + 1
        print(ans)
    elif cmd == 'GETMIN':
        ans = min(range(n), key=lambda x: (dr[x] * dc[x].count(1), x)) + 1
        print(ans)