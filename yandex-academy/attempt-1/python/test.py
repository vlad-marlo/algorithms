def solution(a: int, b: int) -> tuple[int, int]:
    return a + b, a * b


def main() -> None:
    a, b = map(int, (input() for _ in range(2)))
    print(*solution(a, b), sep='\n')


if __name__ == '__main__':
    main()
