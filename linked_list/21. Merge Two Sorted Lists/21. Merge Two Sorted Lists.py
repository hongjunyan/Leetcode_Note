# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        cur.val = 1
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

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
    testcase = [(([1,2,4], [1,3,4]), [1,1,2,3,4,4]),
                (([], []), []),
               ]
    for idx, t in enumerate(testcase):
        first = create_list(t[0][0])
        second = create_list(t[0][1])
        head = func(first, second)
        res = get_list(head)
        pass_flag = t[1] == res
        msg = "pass" if pass_flag else f"wrong, expect {t[1]}, but get {res}"
        print(f"Case {idx}: {msg}")


if __name__ == "__main__":
    sol = Solution()
    unit_test(sol.mergeTwoLists)