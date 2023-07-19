class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* slow,*fast,*entry;
        slow=head;
        fast=head;
        entry=head;
        while(fast!=NULL&& fast->next!=NULL)
        {
         slow=slow->next;
         fast=fast->next->next;
        if(slow == fast) {
            while(slow != entry) {
                slow = slow->next;
                entry = entry->next;
            }
            return slow;
        }
         }
        return NULL;
    }
};