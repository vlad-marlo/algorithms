def algo(num: int) -> str:
    s = str(num)
    grp1 = int(s[0]) + int(s[2]) + int(s[4]) 
    grp2 = int(s[1]) + int(s[3])
    return f'{min(grp1, grp2)}{max(grp1, grp2)}'

assert (res := algo(63179)) == '1016', f'got: {res} want: "1016"'


for i in range(10**4, 10**5):
    if algo(i) == '723':
        print(i)
        break

