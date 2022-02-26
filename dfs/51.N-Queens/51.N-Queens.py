from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # nlog(n) + 2**n, n is the size of candidates

        cnadidates = candidates.sort()  # nlog(n)

        res = []

        def dfs(idx: int, cur: list, cur_sum):
            if cur_sum == target:
                res.append(cur.copy())
                return
            if cur_sum > target or idx >= len(candidates):
                return

            pres = None
            for i in range(idx, len(candidates)):
                cand = candidates[i]
                if cand == pres:
                    continue

                cur.append(cand)
                dfs(i + 1, cur, cur_sum + cand)
                cur.pop()
                pres = cand

        dfs(0, [], 0)
        return res


def unit_test(func):

    testcase = [(([10,1,2,7,6,1,5], 8), [[1,1,6],[1,2,5],[1,7],[2,6]]),
                (([2,5,2,1,2], 5), [[1,2,2],[5]]),
               ]
    for idx, t in enumerate(testcase):
        res = func(*t[0])
        pass_flag = res == t[1]
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.combinationSum2)
