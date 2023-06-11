from typing import List, Optional, cast, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_list_node(l: List[int]) -> Optional[ListNode]:
    if len(l) == 0:
        return None

    head = ListNode(l[0])
    cur = head
    for i in range(1, len(l)):
        cur.next = ListNode(l[i])
        cur = cur.next

    return head


def list_node_to_list(l: Optional[ListNode]) -> List[int]:
    if l == None:
        return []

    head = l
    ret = [head.val]
    while head.next != None:
        head = head.next
        ret.append(head.val)

    return ret


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None

        if k == 1:
            return head

        # count number of nodes
        count = 0
        next = head
        while next != None:
            next = next.next
            count += 1

        if count < k:
            return head

        div_k = count // k

        prev = None
        cur = head
        next = cast(ListNode | None, cur.next)
        cur.next = None
        if next == None:
            return cur

        first_first = None
        last_last = None
        last = None
        for i in range(0, div_k):
            last_last = last
            last = cur
            for j in range(1, k):
                prev = cur
                cur = next
                next = cast(ListNode, cur.next)
                cur.next = prev

            if i == 0:
                first_first = cur

            first = cur
            if last_last != None:
                last_last.next = first

            last.next = next
            cur = next
            next = cast(ListNode, cur.next)

        return first_first


def main():
    # print(
    #     list_node_to_list(
    #         Solution().reverseKGroup(list_to_list_node([1, 2, 3, 4, 5]), 2)
    #     )
    # )
    # print(
    #     list_node_to_list(
    #         Solution().reverseKGroup(list_to_list_node([1, 2, 3, 4, 5]), 3)
    #     )
    # )
    print(list_node_to_list(Solution().reverseKGroup(list_to_list_node([1, 2]), 2)))


if __name__ == "__main__":
    main()
