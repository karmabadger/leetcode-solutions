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
        if head == None or k == 1:
            return head

        count = count_nodes(head)
        if count < k:
            return head

        div_k = count // k
        gfirst = head
        (glast, next) = reverse_k(gfirst, k)
        first = glast
        prev_gfirst = gfirst

        if div_k > 1:
            for i in range(1, div_k):
                gfirst = next
                (glast, next) = reverse_k(gfirst, k)
                prev_gfirst.next = glast
                prev_gfirst = gfirst

            gfirst.next = next
        else:
            gfirst.next = next

        return first


def count_nodes(head: Optional[ListNode]) -> int:
    # count number of nodes
    count = 0
    next = head
    while next != None:
        next = next.next
        count += 1

    return count


def reverse_k(start: ListNode, k: int) -> Tuple[ListNode, ListNode]:
    # reverses and returns the last node and the one after or None
    prev = None
    cur = start
    next = cast(ListNode, cur.next)
    for i in range(k - 1):
        cur.next = prev
        prev = cur
        cur = next
        next = cast(ListNode, cur.next)

    cur.next = prev
    prev = cur
    cur = next

    return (prev, cur)


def main():
    print(
        list_node_to_list(
            Solution().reverseKGroup(list_to_list_node([1, 2, 3, 4, 5]), 2)
        )
    )
    print(
        list_node_to_list(
            Solution().reverseKGroup(list_to_list_node([1, 2, 3, 4, 5]), 3)
        )
    )
    print(list_node_to_list(Solution().reverseKGroup(list_to_list_node([1, 2]), 2)))


if __name__ == "__main__":
    main()
