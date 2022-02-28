from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pre_map = {crs: [] for crs in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visit_set = set()  # all course along the current dfs path

        def dfs(crs: int) -> bool:
            if crs in visit_set:
                # we get loop in graph
                return False

            if pre_map[crs] == []:
                return True

            visit_set.add(crs)
            for pre_crs in pre_map[crs]:
                if not dfs(pre_crs):
                    return False

            visit_set.remove(crs)
            pre_map[crs] = []

            return True

        # the resaon we use loop to check is
        # mainly because what if the graph is not fully connected like
        # for example,
        # 1 -> 2
        # 3 -> 4

        for crs in pre_map:
            if not dfs(crs): return False
        return True


def unit_test(func):

    testcase = [((2, [[1,0]]), True),
                ((2, [[1,0],[0,1]]), False),  # have loop
                ((3, [[0, 1], [1, 2], [2, 0]]), False),  # have loop
                ((5, [[0,1], [0,2], [1,3], [1,4], [3,4]]), True)
               ]
    for idx, t in enumerate(testcase):
        res = func(*t[0])
        pass_flag = res == t[1]
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.canFinish)
