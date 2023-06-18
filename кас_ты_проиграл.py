s: str = open('24_7.txt').readline()
letters = set(s)

for a in letters:
    s = s.replace(
        3 * a, a.lower()
    ).replace(
        a.lower() + 2 * a, a.lower() + a
    ).replace(
        2 * a + a.lower(), a + a.lower()
    ).replace(
        2 * a, ' '
    )
print(letters)
s = ' ' + s + ' '
for a in letters:
    for b in letters:
        for c in letters:
            s = s.replace(a + b + c, f'{a} {c}').replace(f'{a}{c}', f'{a} {c}').replace(f'{a}{b.lower()}{c}',
                                                                                        ' ' + b.lower() + ' ')
    s = s.replace(' ' + a + ' ', ' ')
for _ in range(2):
    for i in letters:
        s = s.replace(f' {i} ', ' ')
        for c in letters:
            s = s.replace(f' {i}{c} ', ' ')
res = max(s.split(), key=len)
for i in range(1, len(res)):
    for letter in letters:
        s = s.replace(' ' + letter.lower() * i + letter, ' ' + letter.lower() * i).replace(
            letter.lower() * i + letter + ' ', letter.lower() * i + ' ')
for letter in letters:
    s = s.replace(letter, ' ')
answer = max([i for i in s.split()], key=len)
print(answer, 3 * len(answer))
