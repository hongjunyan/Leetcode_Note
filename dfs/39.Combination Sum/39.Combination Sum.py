from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, cur: list, total: int) -> None:
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

    def best_combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, cur: list, cur_sum: int) -> None:
            if cur_sum == target:
                res.append(cur.copy())
                return
            if cur_sum > target or i > len(candidates):
                return

            for idx in range(i, len(candidates)):
                cur.append(candidates[idx])
                dfs(idx, cur, cur_sum + candidates[idx])
                cur.pop()

        dfs(0, [], 0)
        return res


def unit_test(func):

    testcase = [(([2,3,6,7], 7), [[2,2,3],[7]]),
                (([2,3,5], 8), [[2,2,2,2],[2,3,3],[3,5]]),
                (([2], 1), []),
               ]
    for idx, t in enumerate(testcase):
        res = func(*t[0])
        pass_flag = res == t[1]
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.combinationSum)
    unit_test(sol.best_combinationSum)
