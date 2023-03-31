def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(file.readline()) for _ in range(int(file.readline()))]


def solution(data: list[int]) -> int:
    primes = [0, len(data)]
    for i in range(len(data)):
        now = data[i]
        for div in range(2, int(now ** 0.5) + 1):
            if now % div == 0:
                break
        else:
            primes.append(i)
    return max([sum(data[primes[i]:primes[i+1]]) for i in range(len(primes) - 1)])


if __name__ == '__main__':
    print(solution(read_data('27A_2.txt')), solution(read_data('27B_2.txt')))
