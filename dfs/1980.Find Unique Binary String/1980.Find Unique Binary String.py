from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        sol = []

        def backtrack(i, ans):
            if i == len(nums):
                ans = "".join(sol)
                if ans not in nums:
                    return ans
                return ""

            for ele in ["0", "1"]:
                if ans == "":
                    sol.append(ele)

                    ans = backtrack(i + 1, ans)

                    sol.pop()
            return ans

        return backtrack(0, "")


def unit_test(func):

    testcase = [(["01","10"], ["00", "11"]),
                (["00","01"], ["10", "11"]),
               ]
    for idx, t in enumerate(testcase):
        res = func(t[0])
        pass_flag = res in t[1]
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.findDifferentBinaryString)
