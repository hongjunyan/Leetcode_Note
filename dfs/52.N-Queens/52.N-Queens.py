from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        visited_col = set()
        visited_posdiag = set()
        visited_negdiag = set()

        def is_not_under_attack(r, c):
            if c not in visited_col and \
                    (r + c) not in visited_posdiag and \
                    (r - c) not in visited_negdiag:
                return True
            return False

        def place_queen(r, c):
            # mark the attacking zone
            visited_col.add(c)
            visited_posdiag.add(r + c)
            visited_negdiag.add(r - c)

        def remove_queen(r, c):
            visited_col.remove(c)
            visited_posdiag.remove(r + c)
            visited_negdiag.remove(r - c)

        def backtrack(r: int, count: int):
            if r == n:
                # we reach the bottom, i.e. we find a solution!
                return count + 1

            for c in range(n):
                if is_not_under_attack(r, c):
                    # place_queen
                    place_queen(r, c)

                    # we move on to the next row
                    count = backtrack(r + 1, count)

                    # backtrack, i.e. remove the queen and remove the attacking zone.
                    remove_queen(r, c)
            return count
        count = backtrack(0, 0)
        return count


def unit_test(func):

    testcase = [(4, 2),
                (1, 1),
               ]
    for idx, t in enumerate(testcase):
        res = func(t[0])
        pass_flag = res == t[1]
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.totalNQueens)
