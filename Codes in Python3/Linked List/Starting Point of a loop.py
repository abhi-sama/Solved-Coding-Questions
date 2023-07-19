class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        entry=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                while slow!=entry:
                    slow=slow.next
                    entry=entry.next
                if slow==entry:
                    return slow

        return None    