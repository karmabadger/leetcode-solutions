from typing import List, Optional, cast, Tuple
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # heaq_list= cast(list[tuple[int, ListNode],[])
        heaq_list: list[tuple[int, ListNode]] = []
        while True:
            all_false = True
            for list_node in lists:
                if list_node != None:
                    heaq_list.append((list_node.val, list_node))
                    all_false = False

            if all_false:
                break

        head = heapq.heappop(heaq_list)[1]
        cur = head
        for i in range(1, len(heaq_list)):
            cur.next = heapq.heappop(heaq_list)[1]
            cur = cur.next

        return head


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
