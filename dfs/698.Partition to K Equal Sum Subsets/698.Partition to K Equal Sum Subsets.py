from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        visited = [False] * len(nums)
        target_sum = sum(nums) / k
        len_num = len(nums)
        # some trick to speed up
        if sum(nums) % k != 0:
            return False

        nums.sort(reverse=True)  # descending

        def backtrack(k: int, sid: int, cur_sum: int) -> bool:
            if k == 1:
                return True

            if cur_sum == target_sum:
                return backtrack(k - 1, 0, 0)

            for i in range(sid, len_num):
                if visited[i] or cur_sum + nums[i] > target_sum:
                    continue
                visited[i] = True
                if backtrack(k, i + 1, cur_sum + nums[i]):
                    return True
                visited[i] = False
            return False

        return backtrack(k, 0, 0)


def unit_test(func):

    testcase = [(([3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269], 5), True),
                (([724,3908,1444,522,325,322,1037,5508,1112,724,424,2017,1227,6655,5576,543], 4), True),
                (([85,35,40,64,86,45,63,16,5364,110,5653,97,95], 7), False),
               ]
    for idx, t in enumerate(testcase):
        res = func(*t[0])
        pass_flag = res == t[1]
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.canPartitionKSubsets)
