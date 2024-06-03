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
        ListNode *temp, *prev, *current;
        temp = NULL;
        prev = NULL;
        current = head;
        while (current) {
            temp = current->next;
            current->next = prev;
            prev = current;
            current = temp;
        }
        return prev;
    }

    int pairSum(ListNode* head) {
        if (head->next->next == NULL)
            return (head->val + head->next->val);
        ListNode* slow = head;
        ListNode* fast = head->next->next;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* ptr1 = head;
        ListNode* ptr2 = reverseList(slow->next);
        int res = 0;
        while (ptr2) {
            int sum = ptr1->val + ptr2->val;
            res = max(sum, res);
            ptr1 = ptr1->next;
            ptr2 = ptr2->next;
        }
        return res;
    }
};