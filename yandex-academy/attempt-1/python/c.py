class DataCenter:
    def __init__(self, index: int, servers_qt: int):
        self.index: int = index
        self.server_qt: int = servers_qt
        self.server_list: list[int] = [1 for _ in range(servers_qt)]
        self.reset_qt: int = 0

    def disable(self, server_number: int) -> None:
        self.server_list[server_number - 1] = 0

    def reset(self) -> None:
        self.server_list = [1 for _ in range(self.server_qt)]
        self.reset_qt += 1

    def get_stat(self):
        return self.reset_qt * sum(self.server_list)

    def __gt__(self, other):
        if self.get_stat() == other.get_stat():
            return self.index < other.index
        return self.get_stat() > other.get_stat()

    def __lt__(self, other):
        if self.get_stat() == other.get_stat():
            return self.index < other.index
        return self.get_stat() < other.get_stat()

    def get_index(self):
        return self.index


def main():
    n, m, q = map(int, input().split())
    data_centers = [DataCenter(i, m) for i in range(1, m + 1)]

    for command in (input() for _ in range(q)):
        match command.split():
            case 'DISABLE', i, j:
                i = int(i) - 1
                j = int(j)
                data_centers[i].disable(j)
            case 'RESET', i:
                i = int(i) - 1
                data_centers[i].reset()
            case 'GETMAX', *_:
                print(max(data_centers).get_index())
            case 'GETMIN', *_:
                print(min(data_centers).get_index())
        # print(*map(lambda x: x.reset_mul_server_on(), data_centers))


if __name__ == '__main__':
    main()
