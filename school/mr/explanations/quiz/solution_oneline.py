print([
    n for n in range(100) if not any(
        sum(map(int, ('>' + '0' * 39 + '1' * n + 39 * '2').replace('>1', '22>', 1).replace('>2', '2>', 1)
                .replace('>0', '1>', 1).replace('>', ''))) % i == 0 for i in
        range(2, int(sum(map(int, ('>' + '0' * 39 + '1' * n + 39 * '2').replace('>1', '22>', 1).replace('>2', '2>', 1)
                             .replace('>0', '1>', 1).replace('>', ''))) ** 0.5) + 1
              ))
])
