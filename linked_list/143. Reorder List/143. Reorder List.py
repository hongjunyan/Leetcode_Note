# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second to last
        second = slow.next
        slow.next = None
        prev, cur = None, second
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        second = prev

        # merge two half
        first = head
        while second:
            next_sec = second.next
            next_fst = first.next
            first.next = second
            second.next = next_fst

            first = next_fst
            second = next_sec


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
    testcase = [([1,2,3,4], [1,4,2,3]),
                ([1], [1]),
                ([1,2,3,4,5], [1,5,2,4,3])
               ]
    for idx, t in enumerate(testcase):
        head = create_list(t[0])
        func(head)
        res = get_list(head)
        pass_flag = t[1] == res
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.reorderList)