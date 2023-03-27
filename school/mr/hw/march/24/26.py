with open('26_5643.txt') as f:
    n, m = map(int, f.readline().split())
    boxes = []
    keys = []
    for i in range(m):
        box, key = map(int, f.readline().split())
        boxes.append(box)
        keys.append(key)
    for i in range(n - m):
        boxes.append(int(f.readline()))
    boxes = [i for i in boxes if i in keys]
    boxes.sort()
    ans = [min([i for i in boxes if i % 2 != 0])]
    for box in boxes:
        if ans[-1] % 2 != box % 2 and ans[-1] + 9 <= box:
            ans.append(box)
    print(ans[0], len(ans))
