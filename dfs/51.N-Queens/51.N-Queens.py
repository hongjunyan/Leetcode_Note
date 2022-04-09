from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        visited_col = set()
        visited_posdiag = set()
        visited_negdiag = set()
        res = []
        board = [["."] * n for r in range(n)]

        def is_not_under_attack(r, c):
            if c not in visited_col and \
                    (r + c) not in visited_posdiag and \
                    (r - c) not in visited_negdiag:
                return True
            return False

        def place_queen(r, c):
            # explore this partial candidate solution,
            board[r][c] = "Q"

            # mark the attacking zone
            visited_col.add(c)
            visited_posdiag.add(r + c)
            visited_negdiag.add(r - c)

        def remove_queen(r, c):
            board[r][c] = "."
            visited_col.remove(c)
            visited_posdiag.remove(r + c)
            visited_negdiag.remove(r - c)

        def backtrack(r: int):
            if r == n:
                # we reach the bottom, i.e. we find a solution!
                sol = ["".join(row) for row in board]
                res.append(sol)
                return

            for c in range(n):
                if is_not_under_attack(r, c):
                    # place_queen
                    place_queen(r, c)

                    # we move on to the next row
                    backtrack(r + 1)

                    # backtrack, i.e. remove the queen and remove the attacking zone.
                    remove_queen(r, c)

        backtrack(0)
        return res

def unit_test(func):

    testcase = [(4, [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]),
                (1, [["Q"]]),
               ]
    for idx, t in enumerate(testcase):
        res = func(t[0])
        pass_flag = sorted(res) == sorted(t[1])
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.solveNQueens)
