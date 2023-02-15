# https://lms.webium.ru/course/292/content/homework/acb435c9-fc00-4a8a-9e08-77c8725d04f7/?taskId=20932


def f(a: int, x: int, y: int) -> bool:
    return (((x + a) > 180) <= (a & 36 == 0)) or ((y % 12 == 0) and (x % 36 != 0))


for a in reversed(range(1, 101)):
    if all(f(a, x, y) for x in range(100) for y in range(100)):
        print(a)
        break
