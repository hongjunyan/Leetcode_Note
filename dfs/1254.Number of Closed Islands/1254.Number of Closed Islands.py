import collections
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = ((0, -1), (0, 1), (-1, 0), (1, 0))

        def dfs(r: int, c: int, val: int):
            if r in range(rows) and c in range(cols) and grid[r][c] == 0:
                grid[r][c] = val
                for dr, dc in directions:
                    dfs(r + dr, c + dc, val)

        # Fill all the land including the boundary with 1
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0 or r == rows - 1 or c == cols - 1) and (grid[r][c] == 0):
                    dfs(r, c, 1)

        # Calculate the number of island
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dfs(r, c, 1)
                    islands += 1
        return islands

    def closedIsland_dfs_with_condition(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        islands = 0
        directions = ((0, -1), (0, 1), (-1, 0), (1, 0))

        def dfs(row, col, isclosed):
            grid[row][col] = -1
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r in range(rows) and c in range(cols) and grid[r][c] == 0:
                    isclosed = dfs(r, c, isclosed)

            # 如果不要這行條件判斷，就是leetcode 200
            if row == 0 or col == 0 or row == rows - 1 or col == cols - 1:
                return False

            return isclosed

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    if dfs(r, c, True):
                        islands += 1
        return islands

    def closedIsland_bfs(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        islands = 0
        directions = ((0, -1), (0, 1), (-1, 0), (1, 0))

        def bfs(r: int, c: int) -> bool:
            q = collections.deque()
            grid[r][c] = -1
            q.append((r, c))
            isclosed = True

            while q:
                row, col = q.popleft()  # 如果要改成dfs，只要改成q.pop()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 0:
                        grid[r][c] = -1
                        q.append((r, c))

                if isclosed and (row == 0 or col == 0 or row == rows - 1 or col == cols - 1):
                    isclosed = False
            return isclosed

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    if bfs(r, c):
                        islands += 1
        return islands

def unit_test(func):
    grid1 = [
        [1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]
    ]
    grid2 = [
        [0,0,1,0,0],
        [0,1,0,1,0],
        [0,1,1,1,0]
    ]

    grid3 = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]
    testcase = [(grid1, 2),
                (grid2, 1),
                (grid3, 2)
               ]
    for idx, t in enumerate(testcase):
        res = func(t[0])
        pass_flag = res == t[1]
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.closedIsland)
    unit_test(sol.closedIsland_dfs_with_condition)
    unit_test(sol.closedIsland_bfs)
