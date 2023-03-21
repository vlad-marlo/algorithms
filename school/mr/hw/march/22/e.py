def read_data() -> tuple[int, int, list[int]]:
    """
    :return first - low cost; second - high price:
    """
    with open('5.txt') as file:
        n, k, m = map(int, file.readline().split())
        return k, m, [int(file.readline()) for _ in range(n)]


low_limit, high_limit, data = read_data()
data.sort()
low = data[:low_limit]
high = data[len(data) - high_limit:]
assert len(low) == low_limit and len(high) == high_limit

print(min(high), sum(low) // len(low))
assert all(i > j for i in high for j in low)
# 27700 7896
