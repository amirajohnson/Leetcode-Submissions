/* Prompt:
Given the head of a singly linked list, reverse the list, and return the reversed list.
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head){
    //return the reversed linked list -> O(1) space
    struct ListNode *prev = NULL;
    struct ListNode *current = head;
    struct ListNode *forward = NULL;
    while (current != NULL){
        forward = current->next;
        current->next = prev;
        prev = current;
        current = forward;
    }
    head = prev;
    return head;
}
