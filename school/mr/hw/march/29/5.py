def algo(n: int) -> int:
    b = bin(n)[2:]
    b = '1'+b+'00' if n % 2 == 0 else b + bin(b.count('1'))[2:]
    return int(b, 2)

assert algo(4) == 48, f'got: {algo(4)}; want: 48'
assert algo(13) == 55, f'got: {algo(13)}; want: 55'

data = {i: res for i in range(2,1000) if (res := algo(i)) > 190}
mm = min(data.values())
for k, v in data.items():
    if v == mm:
        print(k, v)
