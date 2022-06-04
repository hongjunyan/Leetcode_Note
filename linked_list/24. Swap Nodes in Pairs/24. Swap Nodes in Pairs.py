# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur and cur.next:
            nxt_pair = cur.next.next
            sec = cur.next

            sec.next = cur
            cur.next = nxt_pair
            prev.next = sec

            prev = cur
            cur = nxt_pair

        return dummy.next


def create_list(vals: list) -> ListNode:
    dummy = ListNode()
    cur = dummy
    for val in vals:
        newnode = ListNode(val=val)
        cur.next = newnode
        cur = newnode
    return dummy.next


def get_list(head: ListNode) -> list:
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals


def unit_test(func):
    testcase = [([1,2,3,4], [2,1,4,3]),
                ([], []),
                ([1], [1]),
               ]
    for idx, t in enumerate(testcase):
        head = create_list(t[0])
        head = func(head)
        res = get_list(head)
        pass_flag = t[1] == res
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.swapPairs)