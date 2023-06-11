from typing import List, Optional, cast, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur_i = min_list_tour(lists)
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


def min_list_tour(lists: List[Optional[ListNode]]) -> int:
    # mapped = [None if x == None else (x.val, i) for i, x in enumerate(lists)]

    n_list = cast(
        List[Tuple[int, int]],
        list(
            filter(
                lambda x: x != None,
                map(
                    lambda x: None if x[1] == None else (x[1].val, x[0]),
                    enumerate(lists),
                ),
            )
        ),
    )
    n = len(n_list)

    if n == 0:
        return -1

    while n > 1:
        n_div_2 = n // 2
        for i in range(n_div_2):
            index = i * 2
            n_list[i] = (
                n_list[index]
                if n_list[index][0] <= n_list[index + 1][0]
                else n_list[index + 1]
            )

        if n % 2 == 0:
            n = n_div_2
        else:
            n_list[n_div_2] = n_list[(n_div_2) * 2]
            n = n_div_2 + 1

    return n_list[0][1]


def main():
    print(
        list_node_to_list(
            Solution().mergeKLists(
                list(map(list_to_list_node, [[1, 4, 5], [1, 3, 4], [2, 6]]))
            )
        )
    )
    print(list_node_to_list(Solution().mergeKLists(list(map(list_to_list_node, [])))))
    print(list_node_to_list(Solution().mergeKLists(list(map(list_to_list_node, [[]])))))
    print(list_node_to_list(Solution().mergeKLists(list(map(list_to_list_node, [])))))


if __name__ == "__main__":
    main()
