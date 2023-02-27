import string

alphabet = string.digits + string.ascii_uppercase

for p in range(10, 37):
    local = alphabet[:p]
    assert len(local) == p
    for x in local:
        for y in local:
            if int(f'32{x}8', p) + int(f'{x}{x}{x}9', p) == int(f'{y}{y}02', p):
                print(int(f'{y}{y}{x}', p), p)
