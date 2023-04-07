def read_data() -> tuple[int, list[tuple[int, str]]]:
    with open('26.txt') as file:
        n, sm = map(int, file.readline().split())
        res: list[tuple[int, str]] = []
        for _ in range(n):
            price, group = file.readline().strip().split()
            res.append((int(price), group ))
        return sm, res


def solution(sm: int, data: list[tuple[int, str]]) -> tuple[int, int]:
    count, price = 0, 0
    count_a = 0
    a = [data[i][0] for i in range(len(data)) if data[i][1] == 'A']
    b = [data[i][0] for i in range(len(data)) if data[i][1] == 'B']
    a.sort()
    b.sort()
    data.sort(key= lambda x: x[0])
    for i in data:
        if (res := i[0] + price) <= sm:
            price = res
            count += 1
            count_a += i[1] == 'A'
        else:
            break
    now = 0
    a_count = 0
    for i in a:
        if (res := now + i) <= sm:
            a_count += 1
            now = res
        else:
            break
    b_count = 0
    b_sum =0
    for i in b:
        if b_count + a_count >= count:
            break
        if (b_sum + now) < sm:
            b_sum += i
        else:
            break
    return count_a, sm - b_sum - now


if __name__ == '__main__':
    print(solution(*read_data()))
