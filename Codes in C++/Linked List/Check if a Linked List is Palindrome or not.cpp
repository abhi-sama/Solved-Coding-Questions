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
    ListNode* reverse(ListNode* head)
    {
        if(!head||!head->next)
            return head;
        ListNode* temp=reverse(head->next);
        head->next->next=head;
        head->next=NULL;
        return temp;
    }
    bool isPalindrome(ListNode* head) {
        ListNode* s,*f;
        s=head;
        f=head;
        if(!head||!head->next)
            return true;
        while(f->next!=NULL&&f->next->next!=NULL)
        {
            s=s->next;
            f=f->next->next;
        }
        f=reverse(s->next);
        s=head;
        while(f!=NULL)
        {   if(s->val!=f->val)return false;
            s=s->next;
            f=f->next;
        }
        return true;
    }
};