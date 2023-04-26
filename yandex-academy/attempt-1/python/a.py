COMMAND_GET_MAX = "GETMAX"
COMMAND_DISABLE = "DISABLE"
COMMAND_RESET = "RESET"
COMMAND_GET_MIN = "GETMIN"


def read_data() -> tuple[int, int, list[list[str | int]]]:
    n, m, q = map(int, (input().split()))
    res = [[] for _ in range(q)]
    for i in range(q):
        command, *args = input().split()
        if command.upper() in (COMMAND_GET_MIN, COMMAND_GET_MAX):
            res[i].append(command)
        elif command.upper() == COMMAND_RESET:
            res[i].append(command)
            res[i].append(int(args[0]))
        else:
            res[i].append(command)
            res[i].append(int(args[0]))
            res[i].append(int(args[1]))
    return n, m, res


def solution(count_of_centres: int, servers_per_centre: int, commands: list[str | int]) -> None:
    BEFORE = [1 for _ in range(servers_per_centre)]
    data = [[BEFORE, 0, i + 1] for i in range(count_of_centres)]
    for command, *args in commands:
        i: int
        if command == COMMAND_GET_MAX:
            mx = float('-inf')
            mx_index = 0
            for servers, count, index in data:
                if mx < (res := sum(servers) * count):
                    mx = res
                    mx_index = index
            print(mx_index)
        elif command == COMMAND_GET_MIN:
            mx = float('inf')
            mx_index = 0
            for servers, count, index in data:
                if mx > (res := sum(servers) * count):
                    mx = res
                    mx_index = index
            print(mx_index)
        elif command == COMMAND_RESET:
            i = args[0] - 1
            data[i][0] = BEFORE
            data[i][1] += 1
        elif command == COMMAND_DISABLE:
            i, j = args
            i -= 1
            j -= 1
            data[i][0][j] = 0
        else:
            raise Exception('unknown command: %s' % command)


def solution_new(count_of_centres: int, servers_per_centre: int, commands: list[int | str]) -> None:
    before = [1 for _ in range(servers_per_centre)]
    centres = [[before, 0, i + 1] for i in range(count_of_centres)]
    for command, *args in commands:
        if command == COMMAND_GET_MAX:
            print(max(centres, key=lambda x: (sum(x[0]) * x[1], -x[2]))[2])
        elif command == COMMAND_GET_MIN:
            print(min(centres, key=lambda x: (sum(x[0]) * x[1], x[2]))[2])
        elif command == COMMAND_RESET:
            i = args[0] - 1
            centres[i][0] = before
            centres[i][1] += 1
            assert i + 1 == centres[i][2]
        elif command == COMMAND_DISABLE:
            i, j = args
            i -= 1
            j -= 1
            assert i + 1 == centres[i][2]
            centres[i][0][j] = 0
        else:
            raise Exception('unknown command: %s' % command)


if __name__ == '__main__':
    solution(*read_data())
