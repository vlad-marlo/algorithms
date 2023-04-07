def read_data(filename: str) -> list[int]:
    with open(filename) as file:
        return [int(x) for x in file.readlines()]
