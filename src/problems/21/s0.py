from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_listnode(l: list) -> Optional[ListNode]:
    if len(l) == 0:
        return None
    head = ListNode(l[0])
    prev = head
    for i in range(1, len(l)):
        cur = ListNode(l[i])
        prev.next = cur
        prev = cur
    return head


def listnode_to_list(l: Optional[ListNode]) -> list:
    if l == None:
        return []
    res = []
    cur = l
    while cur != None:
        res.append(cur.val)
        cur = cur.next
    return res


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        head = None
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        prev = head
        cur = None
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                cur = list1
                list1 = list1.next
            else:
                cur = list2
                list2 = list2.next

            prev.next = cur
            prev = cur

        if list1 != None:
            prev.next = list1
        elif list2 != None:
            prev.next = list2

        return head


# test it out
def main():
    s = Solution()
    print(
        listnode_to_list(
            s.mergeTwoLists(list_to_listnode([1, 2, 4]), list_to_listnode([1, 3, 4]))
        )
    )
    print(listnode_to_list(s.mergeTwoLists(list_to_listnode([]), list_to_listnode([]))))
    print(
        listnode_to_list(s.mergeTwoLists(list_to_listnode([]), list_to_listnode([0])))
    )


if __name__ == "__main__":
    main()
