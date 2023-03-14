with open('24_6757.txt') as f:
    s = f.read().strip()
    for i in ['CFE', 'FCE']:
        s = s.replace(i, 'x')
    c = 0
    local = 0
    for i in range(len(s)):
        if s[i] == 'x':
            local += 1
            c = max(c, local)
        else:
            local = 0
    print(c)
