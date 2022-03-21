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
    # TODO method2
