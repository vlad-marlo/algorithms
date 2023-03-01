def algo(_s: str) -> str:
    while '111' in _s or '222' in _s:
        _s = _s.replace('111', '22', 1)
        _s = _s.replace('222', '1', 1)
    return _s


s = '22'
string = '1' * 200
while '2' in s:
    string += '1'
    s = algo(string)
    print(len(string), s)
print(len(string))
print(algo('1'*205))
