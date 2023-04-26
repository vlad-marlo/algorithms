from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        deq = deque()
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        time = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (now := grid[r][c]) == 2:
                    deq.append([r, c])
                elif now == 1:
                    fresh += 1
        DIRECTIONS = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while fresh > 0 and deq:
            for _ in range(len(deq)):
                r, c = deq.popleft()
                for dr, dc in DIRECTIONS:
                    row, col = r + dr, c + dc
                    if row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    deq.append([row, col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
