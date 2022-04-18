from typing import List


class Solution:
    def restoreIpAddresses_backtracking_list_manipulation(self, s: str) -> List[str]:
        ans = []

        def backtrack(l: int, cur_ip: list):
            if len(cur_ip) == 4 and l == len(s):
                ans.append(".".join(cur_ip))
                return

            if len(cur_ip) > 4:
                return

            for r in range(l, min(l + 3, len(s))):
                if int(s[l:r + 1]) < 256 and (s[l] != "0" or l == r):
                    backtrack(r + 1, cur_ip + [s[l:r + 1]])

        backtrack(0, [])
        return ans

    def restoreIpAddresses_backtracking_str_manipulation(self, s: str) -> List[str]:
        ans = []

        def backtrack(l: int, dots: int, cur_ip: str):
            if dots == 4 and l == len(s):
                ans.append(cur_ip[:-1])
                return

            if dots > 4:
                return

            for r in range(l, min(l + 3, len(s))):
                if int(s[l:r + 1]) < 256 and (s[l] != "0" or l == r):
                    backtrack(r + 1, dots + 1, cur_ip + s[l:r + 1] + ".")

        backtrack(0, 0, "")
        return ans


def unit_test(func):

    testcase = [("25525511135", ["255.255.11.135","255.255.111.35"]),
                ("0000", ["0.0.0.0"]),
                ("101023", ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"])
               ]
    for idx, t in enumerate(testcase):
        res = func(t[0])
        pass_flag = sorted(res) == sorted(t[1])
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.restoreIpAddresses_backtracking_list_manipulation)
    unit_test(sol.restoreIpAddresses_backtracking_str_manipulation)
