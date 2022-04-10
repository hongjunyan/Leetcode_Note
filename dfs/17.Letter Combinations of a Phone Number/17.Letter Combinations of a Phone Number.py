from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        maps = {'2': ["a", "b", "c"],
                "3": ["d", "e", "f"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"],
                }

        ans = []
        cur = []

        def backtrack(i):
            if i == len(digits):
                cur_str = "".join(cur)
                ans.append(cur_str)
                return

            chars = maps[digits[i]]
            for c in chars:
                cur.append(c)

                backtrack(i + 1)

                cur.pop()

        if len(digits):
            backtrack(0)
        return ans


def unit_test(func):

    testcase = [("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
                ("", []),
                ("2", ["a","b","c"])
               ]
    for idx, t in enumerate(testcase):
        res = func(t[0])
        pass_flag = sorted(res) == sorted(t[1])
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.letterCombinations)
