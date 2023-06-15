import math
import time


def timer(f):
    def inner(*args, **kwargs):
        now = time.time_ns()
        res = f(*args, **kwargs)
        print(time.time_ns() - now, res)
        return res

    return inner


def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


@timer
def solution(data: list[int]) -> int:
    mx = 0
    mx_gcd = 0
    sm = sum(data)
    for i in set(data):
        lst = data.copy()
        lst.remove(i)
        gcd = math.gcd(*lst)
        mx_gcd, mx = max((mx_gcd, mx), (gcd, sm - i))
    return mx


@timer
def solution_old(data: list[int]) -> int:
    mx = 0
    mx_gcd = 0
    sm = sum(data)
    for i in range(len(data)):
        lst = data.copy()
        lst.pop(i)
        gcd = math.gcd(*lst)
        mx_gcd, mx = max((mx_gcd, mx), (gcd, sm - data[i]))
    return mx


print(solution(read_data('27A_7358.txt')) == 149395650050484)
print(solution_old(read_data('27A_7358.txt')) == 149395650050484)
print(solution(read_data('27B_7358.txt')) == 154779191650050741)
