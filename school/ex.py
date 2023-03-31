from functools import lru_cache

@lru_cache(None)
def f(a, b):
    if b == 0:
        return a
    if a >= b > 0:
        return f(a-b, b)
    return f(b, a)


for i in range(1234567890123):
    f(i, 14)
c = 0
print('done ')
for i in range(123456795, 1234567889):
    c += f(i, 14) == 1
print(c)
