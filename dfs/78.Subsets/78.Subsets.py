from typing import List


class Solution:
    def subsets_dfs(self, nums: List[int]) -> List[List[int]]:
        # time complexity is O(n*(2^n)), because sum of each layer is 2^0 + 2^1 + 2^2 + ... 2^n == n*2^n
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # selected nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # don't select nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

    def subsets_backtracking(self, nums: List[int]) -> List[List[int]]:
        res = []
        curset = []

        def dfs(sid):
            res.append(curset.copy())

            for i in range(sid, len(nums)):
                curset.append(nums[i])
                dfs(i + 1)
                curset.pop()

        dfs(0)
        return res

    def subsets_backtracking2(self, nums: List[int]) -> List[List[int]]:
        res = []
        curset = []

        def backtrack(sid):
            if len(curset) == k:
                res.append(curset.copy())
                return

            for i in range(sid, len(nums)):
                curset.append(nums[i])
                backtrack(i + 1)
                curset.pop()

        for k in range(len(nums) + 1):
            backtrack(0)  # generate all subsets of length k

        return res

def unit_test(func):

    testcase = [([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
                ([0], [[],[0]]),
               ]
    for idx, t in enumerate(testcase):
        res = func(t[0])
        pass_flag = sorted(res) == sorted(t[1])
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.subsets_dfs)
    unit_test(sol.subsets_backtracking)
    unit_test(sol.subsets_backtracking2)