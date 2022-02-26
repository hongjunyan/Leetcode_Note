class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # O(n*len(count_t))

        window, count_t = {}, {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        def is_t_in_window():
            for c in count_t:
                if window.get(c, 0) < count_t[c]:
                    return False
            return True

        res, min_len = [0, 0], float("inf")
        l = 0
        for r in range(len(s)):
            # add char into window
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            while is_t_in_window():
                # update l,r
                cur_len = r - l + 1
                if cur_len < min_len:
                    min_len = cur_len
                    res = [l, r]
                # reduce window
                window[s[l]] -= 1
                l += 1

        if min_len == float("inf"):
            return ""

        l, r = res
        return s[l:r + 1]

    def best_minWindow(self, s: str, t: str) -> str:
        # O(n)

        window, count_t = {}, {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        have = 0  # the num of chars in t that the window have
        need = len(count_t)
        res, min_len = [0, 0], float("inf")

        l = 0
        for r in range(len(s)):
            # add char into window
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                # update l,r
                cur_len = r - l + 1
                if cur_len < min_len:
                    min_len = cur_len
                    res = [l, r]
                # reduce window
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        if min_len == float("inf"):
            return ""

        l, r = res
        return s[l:r + 1]


def unit_test(func):

    testcase = [(("ADOBECODEBANC", "ABC"), "BANC"),
                (("a", "a"), "a"),
                (("a", "aa"), ""),
               ]
    for idx, t in enumerate(testcase):
        res = func(*t[0])
        pass_flag = res == t[1]
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.minWindow)
    unit_test(sol.best_minWindow)
