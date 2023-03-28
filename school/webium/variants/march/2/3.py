with open('3.csv') as file:
    # file.readline()
    lines = [i.strip().split(';') for i in file.readlines()]
    print(lines[0])
    ans = {}
    for i in lines[1:]:
        if len(i) != 8:
            print(len(i), i)
            continue
        if ans.get(i[7]) is None:
            ans[i[7]] = 0
        ans[i[7]] += int(i[5])
    mx = max(ans.values())
    print(mx/ 2**20)