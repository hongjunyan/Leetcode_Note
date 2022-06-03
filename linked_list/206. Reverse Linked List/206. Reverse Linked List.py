# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        newhead = head
        if head.next is not None:
            newhead = self.reverseList_recursive(head.next)
            head.next.next = head
        head.next = None

        return newhead

    def reverseList_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev


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
    testcase = [([1,2,3,4,5], [5,4,3,2,1]),
                ([1,2], [2,1]),
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
    unit_test(sol.reverseList_recursive)
    unit_test(sol.reverseList_iterative)