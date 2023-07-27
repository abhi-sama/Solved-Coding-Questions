# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return temp

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        fast = self.reverse(slow.next)
        slow = head
        while fast is not None:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
