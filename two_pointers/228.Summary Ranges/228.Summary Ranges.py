from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        res = []
        l = 0
        pres = nums[0] - 1
        for r in range(len(nums)):
            n = nums[r]
            if n - pres != 1:
                # not continues anymore
                if l == r - 1:
                    res.append(f"{nums[l]}")
                else:
                    res.append(f"{nums[l]}->{nums[r - 1]}")
                l = r
            pres = n

        if l == r:
            res.append(f"{nums[r]}")
        else:
            res.append(f"{nums[l]}->{nums[r]}")

        return res

def unit_test(func):

    testcase = [([0,1,2,4,5,7], ["0->2","4->5","7"]),
                ([0,2,3,4,6,8,9], ["0","2->4","6","8->9"]),
                ([-1], ["-1"]),
               ]
    for idx, t in enumerate(testcase):
        res = func(t[0])
        pass_flag = res == t[1]
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.summaryRanges)