from string import octdigits

_min = 10 ** 10

for x in octdigits:
    for y in octdigits:
        res = int(f'36{x}53', 8) - int(f'4{y}3', 8)
        if res < _min:
            print(res, x, y)
            _min = res
