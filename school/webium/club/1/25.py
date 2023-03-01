import fnmatch


def main():
    for num in [num for num in range(10 ** 9) if
                (num + 1) % 3333 == 0 and all(
                    [fnmatch.fnmatch(str(num), mask) for mask in ('?[24680]11*', '*4*', '*?7[13579]')])]:
        for div in range(2, int(num ** 0.5) + 1):
            if num % div == 0:
                break
        else:
            print(num)


if __name__ == '__main__':
    main()
