from typing import List


class Solution:
    def permute_hashmap(self, nums: List[int]) -> List[List[int]]:
        count_dict = {}

        for n in nums:
            count_dict[n] = 1 + count_dict.get(n, 0)

        perm = []
        res = []

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for n in count_dict:
                if count_dict[n] == 0:
                    continue

                count_dict[n] -= 1
                perm.append(n)

                backtrack()

                count_dict[n] += 1
                perm.pop()

        backtrack()
        return res


def unit_test(func):

    testcase = [([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
                ([0,1], [[0,1],[1,0]]),
                ([1], [[1]]),
                ([1,1,2], [[1,1,2],[1,2,1],[2,1,1]])
               ]

    def normalize(ans: list):
        return sorted([str(perm) for perm in ans])

    for idx, t in enumerate(testcase):
        res = func(t[0])
        # convert to List[str] and cast to Set()
        res = normalize(res)
        ans = normalize(t[1])

        pass_flag = res == ans
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.permute_hashmap)  # can handle duplicate ele
