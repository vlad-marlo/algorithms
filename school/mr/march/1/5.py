def read_data() -> str:
    with open('5.txt') as f:
        return f.read()


def solution(data: str) -> int:
    return len(max(data.replace('FF', 'F F').replace('EE', 'E E').replace('D', ' ').split(), key=len))


if __name__ == '__main__':
    print(solution(read_data()))
