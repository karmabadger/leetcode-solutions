from typing import List, Optional, cast


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        count = count_list(head)
        return sort_list(head, count)


def count_list(head: Optional[ListNode]) -> int:
    count = 0
    cur = head
    while cur != None:
        count += 1
        cur = cur.next
    return count


def sort_list(head: ListNode, size: int) -> ListNode:
    if size == 1:
        return head

    # split list into 2 and then recursive calls
    head2 = head
    count = 0
    head2_index = size // 2
    prev = head2
    while count < head2_index:
        prev = head2
        head2 = cast(ListNode, head2.next)
        count += 1

    prev.next = None
    res1 = sort_list(head, head2_index)
    res2 = sort_list(head2, size - head2_index)

    if res1.val < res2.val:
        merged = res1
        res1 = res1.next
    else:
        merged = res2
        res2 = res2.next
    cur = merged
    # merge
    while res1 != None and res2 != None:
        if res1.val < res2.val:
            cur.next = res1
            cur = res1
            res1 = res1.next
        else:
            cur.next = res2
            cur = res2
            res2 = res2.next

    while res1 != None:
        cur.next = res1
        cur = res1
        res1 = res1.next

    while res2 != None:
        cur.next = res2
        cur = res2
        res2 = res2.next

    return merged


def list_to_ListNode(l: List[int]) -> Optional[ListNode]:
    if len(l) == 0:
        return None

    head = ListNode(l[0])
    cur = head
    for i in range(1, len(l)):
        cur.next = ListNode(l[i])
        cur = cur.next

    return head


def listNode_to_list(head: Optional[ListNode]) -> List[int]:
    res = []
    cur = head
    while cur != None:
        res.append(cur.val)
        cur = cur.next

    return res


data = [
    ([4, 2, 1, 3], [1, 2, 3, 4]),
    ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
    ([], []),
]

for input, output in data:
    print(listNode_to_list(Solution().sortList(list_to_ListNode(input))), output)
