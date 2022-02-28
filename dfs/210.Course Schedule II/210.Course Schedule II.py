from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        pre_map = {crs: [] for crs in range(numCourses)}
        for crs, pre_crs in prerequisites:
            pre_map[crs].append(pre_crs)

        visit_set = set()  # all course along the current dfs path
        output_set = set()  # make faster than using list when checking the ele in output
        output = list()

        def dfs(crs: int) -> bool:
            if crs in visit_set:
                # the graph have loop
                return False

            if crs in output_set:
                return True

            visit_set.add(crs)
            for pre_crs in pre_map[crs]:
                if dfs(pre_crs) == False:
                    return False

            visit_set.remove(crs)
            output_set.add(crs)
            output.append(crs)

            return True

        for crs in pre_map:
            if dfs(crs) == False:
                return []
        return output


def unit_test(func):

    testcase = [((4, [[1,0],[2,0],[3,1],[3,2]]), [0,1,2,3]),
                ((1, []), [0]),
                ((3, [[0, 1], [1, 2], [2, 0]]), []),  # have loop
               ]
    for idx, t in enumerate(testcase):
        res = func(*t[0])
        pass_flag = res == t[1]
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.findOrder)
