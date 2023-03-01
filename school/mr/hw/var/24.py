def read_data() -> str:
    with open('24_demo.txt') as file:
        return file.read().strip()


def solution(data: str) -> int:
    __max = 0
    __count = 0
    for i in data:
        if i == "Z":
            __count += 1
        else:
            __max = max(__max, __count)
            __count = 0
    return __max


def main():
    print(solution(read_data()))


if __name__ == '__main__':
    main()
