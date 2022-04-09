from typing import List


class Solution:
    def subsetsWithDup_dfs(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def backtrack(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            # add nums[i] into subset
            subset.append(nums[i])
            backtrack(i + 1)

            # not add nums[i] into subset
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return res

    def subsetsWithDup_hashmap(self, nums: List[int]) -> List[List[int]]:
        res = []
        curset = []

        counts = {}

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        keys = list(counts.keys())

        def backtrack(sid):
            res.append(curset.copy())

            for i in range(sid, len(keys)):
                key = keys[i]
                if counts[key] == 0:
                    continue

                counts[key] -= 1
                curset.append(key)

                backtrack(i)

                counts[key] += 1
                curset.pop()

        backtrack(0)
        return res

def unit_test(func):

    testcase = [([1,2,2], [[],[1],[1,2],[1,2,2],[2],[2,2]]),
                ([0], [[],[0]]),
               ]
    for idx, t in enumerate(testcase):
        res = func(t[0])
        pass_flag = sorted(res) == sorted(t[1])
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.subsetsWithDup_dfs)
    unit_test(sol.subsetsWithDup_hashmap)
