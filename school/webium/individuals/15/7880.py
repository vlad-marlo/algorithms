for file in ('27A_7880.txt', '27B_7880.txt'):
    f = open(file)
    n, k = map(int, (f.readline() for _ in range(2)))

    data = [int(f.readline()) for _ in range(n)]

    ans = 0
    for i in range(len(data)-1):
        for j in range(i + 1,len(data)):
            if j - i > k:
                break
            ans += (j - i <= k) and (data[i] + data[j]) % 17 == 0
    print(ans)
