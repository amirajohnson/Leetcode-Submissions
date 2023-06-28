/**
Prompt:
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteMiddle(struct ListNode* head){
    //step 1: get the length of the linked list
    int len = 0;
    struct ListNode *current = head;
    while (current != NULL){
        len += 1;
        current = current->next;
    }

    int mid = len/2;

    //edgecase, AVOID LEAKING MEMORY
    if (len == 1){
        head = head->next;
        return head;
    }

    //we now have the length of the input linked list.
    //we want to do this in-place
    current = head;
    struct ListNode *prev = current;
    int current_node = 0; //0-indexed
    while (current != NULL){
        if (current_node == mid){
            prev->next = current->next;
            current->next = NULL;
            return head;
        }
        prev = current;
        current = current->next;
        current_node += 1;
    }

    return head;


}
