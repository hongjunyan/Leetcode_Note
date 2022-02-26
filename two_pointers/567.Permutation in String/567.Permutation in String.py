class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window, s1_count = {}, {}

        for i in range(len(s1)):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)
            window[s2[i]] = 1 + window.get(s2[i], 0)

        if s1_count == window:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            # add char at right of window
            window[s2[r]] = 1 + window.get(s2[r], 0)
            # remove char at left of window
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                # keep the size of window is the same as s1_count
                window.pop(s2[l])

            if window == s1_count:
                return True
            l += 1
        return False


def unit_test(func):

    testcase = [(("ab", "eidbaooo"), True),
                (("ab", "eidboaoo"), False),
                (("ab", "a"), False),
               ]
    for idx, t in enumerate(testcase):
        res = func(*t[0])
        pass_flag = res == t[1]
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.checkInclusion)
