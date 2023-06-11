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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        prev = None
        cur = head
        next = cur.next
        cur.next = None

        while next != None:
            prev = cur
            cur = next
            next = cur.next
            cur.next = prev

        return cur


def main():
    print(list_node_to_list(Solution().reverseList(list_to_list_node([1, 2, 3, 4, 5]))))
    print(list_node_to_list(Solution().reverseList(list_to_list_node([1, 2]))))
    print(list_node_to_list(Solution().reverseList(list_to_list_node([]))))


if __name__ == "__main__":
    main()
