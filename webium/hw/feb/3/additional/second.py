# https://lms.webium.ru/course/292/content/homework/acb435c9-fc00-4a8a-9e08-77c8725d04f7/?taskId=20933
import typing

P = [i for i in range(32, 101) if i % 2 == 0]
Q = [30, 45, 60, 75, 90, 105, 120]


def f(a: typing.Iterable, x: int) -> bool:
    return (x not in a) or ((x not in Q) and (x in P)) or (x in Q)


ans = []

for x in range(1000):
    if ((x not in Q) and (x in P)) or (x in Q):
        ans.append(x)
a = [x for x in range(121) if x not in ans]
_count = 0
print(len(a))
for i in a:
    _count += i % 19 == 10
print(a, _count, sep="\n")
