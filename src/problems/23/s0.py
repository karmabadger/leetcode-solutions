from typing import List, Optional, cast, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur_i = min_list(lists)
        if cur_i == -1:
            return None

        cur: ListNode = cast(ListNode, lists[cur_i])
        head = cur

        while True:
            cur_i = min_list_tour(lists)
            if cur_i == -1:
                cur.next = None
                return head

            next = cast(ListNode, lists[cur_i])
            lists[cur_i] = next.next
            cur.next = next
            cur = next


_pos_infinity = float("INF")  # Positive infinity


def min_list(lists: List[Optional[ListNode]]) -> int:
    min_val = _pos_infinity
    min_ind = 0
    all_none = True
    for i, node in enumerate(lists):
        if node != None:
            all_none = False
            if node.val < min_val:
                min_ind = i
                min_val = node.val

    if all_none:
        return -1

    return min_ind


def min_list_tour(lists: List[Optional[ListNode]]) -> int:
    mapped = [None if x == None else (x.val, i) for i, x in enumerate(lists)]
    filtered = filter(lambda x: x != None, mapped)

    n_list = cast(List[Tuple[int, int]], list(filtered))
    n = len(n_list)

    if n == 0:
        return -1

    while n > 1:
        for i in range(0, n, 2):
            tmp = n_list[i] if n_list[i][0] < n_list[i + 1][0] else n_list[i + 1]
            n_list[i] = tmp

        n_div_2 = n // 2
        if n % 2 == 0:
            n = n_div_2
        else:
            n_list[n_div_2] = n_list[(n_div_2 - 1) * 2 + 1]
            n = n_div_2 + 1

    return n_list[0][0]
