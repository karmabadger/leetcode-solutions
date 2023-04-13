/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
  if (list1 == NULL) return list2;
  if (list2 == NULL) return list1;

  struct ListNode* head = NULL;
  if (list1->val < list2->val) {
    head = list1;
    list1 = list1->next;
  } else {
    head = list2;
    list2 = list2->next;
  }

  struct ListNode* cur = head;
  while (list1 != NULL && list2 != NULL){
    if (list1->val < list2->val){
      cur->next = list1;
      list1 = list1->next;
    } else {
      cur->next = list2;
      list2 = list2->next;
    }
    cur = cur->next;
  }

  cur->next = list2;
  if (list1 != NULL) cur->next = list1;

  return head;
}