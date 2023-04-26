s: str
for digit1 in '123':
    for digit2 in '123':
        while f'{digit1}{digit2}' in s:
            s = s.replace(f'{digit1}{digit2}', f'{digit1} {digit2}')
print(len(max(s.split(), key=len)))
