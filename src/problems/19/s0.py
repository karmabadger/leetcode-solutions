from typing import Optional, List, cast


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        bef = head
        cur = head
        for i in range(n):
            if not cur.next:
                return bef.next
            cur = cur.next

        cur = cur.next
        while cur:
            bef: ListNode = cast(ListNode, bef.next)
            cur = cur.next

        after = cast(ListNode, bef.next)
        after = cast(ListNode, after.next)

        bef.next = after

        return head


def from_list(l: List[int]) -> Optional[ListNode]:
    if not l:
        return None
    head = ListNode(l[0])
    cur = head
    for i in range(1, len(l)):
        cur.next = ListNode(l[i])
        cur = cur.next
    return head


def to_list(self: Optional["ListNode"]) -> List[int]:
    res = []
    cur = self
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res


def main():
    print(to_list(Solution().removeNthFromEnd(from_list([1, 2, 3, 4, 5]), 2)))
    print(to_list(Solution().removeNthFromEnd(from_list([1]), 1)))
    print(to_list(Solution().removeNthFromEnd(from_list([1, 2]), 1)))


if __name__ == "__main__":
    main()
