/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *temp,*prev,*current;
        temp=nullptr;
        prev=nullptr;
        current=head;
        while(current)
        {
            temp=current->next;
            current->next=prev;
            prev=current;
            current=temp;
        }
        return prev;
        /*Recursion
        if(!head||!head->next)return head;
        ListNode* temp=reverseList(head->next);
        head->next->next=head;
        head->next=nullptr;
        return temp;
        */
    }
};