COMMAND_GET_MAX = "GETMAX"
COMMAND_GET_MIN = "GETMIN"
COMMAND_DISABLE = "DISABLE"
COMMAND_RESET = "RESET"


def read_data() -> tuple[int, int, list[list[str | int]]]:
    n, m, q = map(int, (input().split()))
    res = [[] for _ in range(q)]
    for i in range(q):
        command, *args = input().split()
        res[i].append(command)
        if command in (COMMAND_GET_MIN, COMMAND_GET_MAX):
            pass
        elif command == COMMAND_RESET:
            res[i].append(int(args[0]) - 1)
        else:
            res[i].append(int(args[0]) - 1)
            res[i].append(int(args[1]) - 1)
    return n, m, res


def sol(count_of_centres, servers_per_centre, commands) -> list[int]:
    BEFORE = [1 for _ in range(servers_per_centre)]
    centres = [[BEFORE[:], 0, servers_per_centre, i + 1] for i in range(count_of_centres)]
    answer = []
    for command, *args in commands:
        if command == COMMAND_RESET:
            i = args[0]
            centres[i][0] = BEFORE[:]
            centres[i][1] += 1
            centres[i][2] = servers_per_centre
        elif command == COMMAND_DISABLE:
            i, j = args
            centres[i][2] -= centres[i][0][j]
            centres[i][0][j] = 0
        elif command == COMMAND_GET_MAX:
            answer.append(max(centres, key=lambda x: (x[1] * x[2], -x[3]))[3])
        elif command == COMMAND_GET_MIN:
            answer.append(min(centres, key=lambda x: (x[1] * x[2], x[3]))[3])
    return answer


if __name__ == '__main__':
    print(*sol(*read_data()), sep='\n')
