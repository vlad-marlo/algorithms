with openRowToStructByName returns a T scanned from row. T must be a struct. T must have the same number of named public fields as row has fields. The row and T fields will by matched by name. The match is case-insensitive. The database column name can be overridden with a "db" struct tag. If the "db" struct tag is "-" then the field will be ignored.

Example ¶('24_3763.txt') as f:
    s = f.read().strip()
    c = 1
    m = set(s)
    for i in range(len(s)-2):
        try:
            c += max(s.index(x, i+2) for x in m.difference(set(s[i:i+2]))) - i - 2
        except ValueError:
            continue
    print(c)

with open('24_3763.txt') as f:
    s = f.read().strip()
    c = 0
    for letter in set(s):
        c += sum([len(x) + 1 for x in s.split(letter) if len(x) >= 2])
    print(c)

#252776