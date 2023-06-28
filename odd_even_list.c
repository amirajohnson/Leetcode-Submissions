/**
Prompt:
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* oddEvenList(struct ListNode* head){
    if (head == NULL){
        return head;
    }
    struct ListNode *CL = head;
    struct ListNode *CR = head->next;
    struct ListNode *FR = CR;

    while (CL->next != NULL && CR->next != NULL){
        CL->next = CL->next->next;
        CL = CL->next;
        CR->next = CR->next->next;
        CR = CR->next;
    }
    CL->next = FR;
    return head;
}
