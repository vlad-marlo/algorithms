def read_data() -> str:
    with open('24.txt') as f:
        return f.read().strip()


def sol(data: str) -> int:
    count = {
        i: 0 for i in set(data)
    }
    indexes = [i + 1 for i in range(len(data) - 2) if data[i] == data[i+2]]
    for i in indexes:
        count[data[i]] += 1
    m = 0
    for k, v in count.items():
        if v > m:
            print(k, v)
            m = v
    print(count)
    return m


sol(read_data())